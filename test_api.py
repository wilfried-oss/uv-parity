from fastapi.testclient import TestClient
from api import app, NumberRequest

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
