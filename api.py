from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def health_check():
    return {"status": "OK"}


@app.get("/")
def welcome_root():
    return {"message": "Welcome to Check Parity API !"}
