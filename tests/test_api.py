# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# verify the /health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# verify the /predict endpoint with valid input
def test_predict():
    data = {"features": [5.1, 3.5, 1.4, 0.2]}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], int)

# verify the /predict endpoint with invalid input
def test_predict_invalid_input():
    data = {"features": [1, 2]}
    response = client.post("/predict", json=data)
    assert response.status_code == 400
    assert "Expected 4 features" in response.json()["detail"]


