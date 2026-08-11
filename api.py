from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from fastapi.staticfiles import StaticFiles

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







@app.post("/check_parity")
def check_parity(request: NumberRequest):
    number = request.number
    return {"number": number, "parity": _ckeck_parity(number)}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
