# Stage 1: build dependencies with uv
FROM python:3.12-slim AS builder

# Install uv (statically linked binary, no need for pip)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy only dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into a project-local virtual environment (.venv)
# --frozen ensures the lockfile is respected exactly, no re-resolving
# --no-install-project skips installing the app itself for now (cache-friendly)
RUN uv sync --frozen --no-install-project --no-dev

# Now copy the actual application code
COPY . .

# Install the project itself into the same venv
RUN uv sync --frozen --no-dev

# Stage 2: slim runtime image
FROM python:3.12-slim

WORKDIR /app

# Copy the virtual environment and app code from the builder stage
COPY --from=builder /app /app

# Make sure the venv's binaries are used (uvicorn, etc.)
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
