from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "johndoe@example.com", "password": "securepass"})
    assert response.status_code == 200
    assert response.json()["email"] == "johndoe@example.com"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
