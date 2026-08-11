from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Check Parity API based on python 3 !"
    }


def test_check_parity():
    response = client.post("/check_parity", json={"number": 4})
    assert response.status_code == 200
    assert response.json() == {"number": 4, "parity": "even"}

    response = client.post("/check_parity", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"number": 5, "parity": "odd"}
