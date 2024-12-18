# User Management API

A simple user management system using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. Fully containerized with **Docker** and integrated with **GitHub Actions** for CI/CD.

## Features

- Create and retrieve users.
- Validation with **Pydantic**.
- PostgreSQL as the database backend.
- Automated tests with **Pytest**.

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd user_management

### 2. Environment Variables
Create a .env file in the root directory and add the following:

env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=myappdb
DATABASE_URL=postgresql+psycopg2://user:password@postgres:5432/myappdb

### 3. Run the Application
docker-compose up -d

### 4. Run Tests
docker-compose exec fastapi pytest --maxfail=1 --disable-warnings