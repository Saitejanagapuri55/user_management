from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from app.db import Base, SessionLocal

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

def create_user(db: SessionLocal, user: UserCreate):
    db_user = User(name=user.name, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: SessionLocal, email: str):
    return db.query(User).filter(User.email == email).first()
