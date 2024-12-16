import pytest
from app.database import SessionLocal

@pytest.fixture
async def db_session():
    async with SessionLocal() as session:
        yield session
