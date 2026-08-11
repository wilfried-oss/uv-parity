from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NumberRequest(BaseModel):
    number: int


def _ckeck_parity(number: int) -> str:
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


@app.get("/healthz")
async def health_check():
    return {"status": "OK"}


@app.get("/")
def welcome_root():
    return {"message": "Welcome to Check Parity API based on python 3 !"}


@app.post("/check_parity")
def check_parity(request: NumberRequest):
    number = request.number
    return {"number": number, "parity": _ckeck_parity(number)}
