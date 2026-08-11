from fastapi.testclient import TestClient
from pydantic import ValidationError
from api import app, NumberRequest
import pytest

client = TestClient(app)


def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_check_parity():
    response = client.post("/check_parity", json={"number": 4})
    assert response.status_code == 200
    assert response.json() == {"number": 4, "parity": "even"}

    response = client.post("/check_parity", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"number": 5, "parity": "odd"}

def test_number_must_be_positive_error_message():
    with pytest.raises(ValidationError) as exc_info:
        NumberRequest(number=-1)
    assert "number must be positive" in str(exc_info.value)
