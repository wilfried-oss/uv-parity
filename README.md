# uv-parity

A tiny FastAPI service that tells you if a number is odd or even. Built mostly as a playground to get comfortable with [uv](https://github.com/astral-sh/uv) for dependency management instead of pip/poetry.

## Why this exists

I wanted a minimal, no-nonsense project to try out uv end to end: locking dependencies, running the app, running tests, all without touching a virtualenv by hand. Parity checking was the simplest possible "business logic" I could wrap an API around, so that's what it does. Don't expect more than that.

## Stack

- Python 3.12+
- FastAPI
- Pydantic
- pytest (via FastAPI's `TestClient`)
- uv for packaging and dependency management

## Getting started

Clone the repo and sync dependencies with uv:

```bash
git clone https://github.com/wilfried-oss/uv-parity.git
cd uv-parity
uv sync
```

Run the API:

```bash
uv run fastapi dev api.py
```

The server starts on `http://127.0.0.1:8000`.

## Endpoints

| Method | Route           | Description                              |
| ------ | --------------- | ---------------------------------------- |
| GET    | `/`             | Welcome message                          |
| GET    | `/healthz`      | Health check, returns `{"status": "OK"}` |
| POST   | `/check_parity` | Takes a number, returns its parity       |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/check_parity \
  -H "Content-Type: application/json" \
  -d '{"number": 7}'
```

Response:

```json
{ "number": 7, "parity": "odd" }
```

## Running tests

```bash
uv run pytest
```

## Notes

This is a learning project, not something meant for production. No auth, no persistence, no rate limiting — just a clean example of a FastAPI app managed with uv, from dependency locking to running tests.
