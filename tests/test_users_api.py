import os
import sys
from app.main import app
from fastapi.testclient import TestClient

# Conditionally set DATABASE_URL
DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql+psycopg2://user:password@localhost:5432/myappdb")
os.environ["DATABASE_URL"] = DATABASE_URL

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "running", "service": "User Management API"}


# 2. Create user
def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com", "password": "secret123"})
    assert response.status_code == 200
    assert response.json()["email"] == "alice@example.com"

# 3. Duplicate user
def test_duplicate_user():
    client.post("/users/", json={"name": "Alice", "email": "alice@example.com", "password": "secret123"})
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com", "password": "secret123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "This email is already registered."

# 4. Empty fields
def test_empty_fields():
    response = client.post("/users/", json={"name": "", "email": "", "password": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Fields cannot be empty"

# 5. Password too short
def test_password_too_short():
    response = client.post("/users/", json={"name": "Bob", "email": "bob@example.com", "password": "123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Password must be at least 6 characters long."

# 6. Invalid email format
def test_invalid_email():
    response = client.post("/users/", json={"name": "Charlie", "email": "invalidemail", "password": "secret123"})
    assert response.status_code == 422  # Pydantic raises validation error

# 7. Retrieve users
def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 8. Create multiple users
def test_create_multiple_users():
    response1 = client.post("/users/", json={"name": "Eve", "email": "eve@example.com", "password": "secret123"})
    response2 = client.post("/users/", json={"name": "Frank", "email": "frank@example.com", "password": "secret456"})
    assert response1.status_code == 200
    assert response2.status_code == 200

# 9. Missing fields
def test_missing_fields():
    response = client.post("/users/", json={"name": "George", "email": "george@example.com"})
    assert response.status_code == 422

# 10. Retrieve users after creation
def test_get_users_after_creating():
    client.post("/users/", json={"name": "Hannah", "email": "hannah@example.com", "password": "hannah123"})
    response = client.get("/users/")
    assert response.status_code == 200
    users = response.json()
    assert any(user["email"] == "hannah@example.com" for user in users)
