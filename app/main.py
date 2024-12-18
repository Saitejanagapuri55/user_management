from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database Configuration
DATABASE_URL = "postgresql+psycopg2://user:password@postgres:5432/myappdb"

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Database Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic Schemas
class UserSchema(BaseModel):
    name: str = Field(..., min_length=1, description="Name cannot be empty")
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters long")

    @field_validator("name", "email", "password")
    def fields_cannot_be_empty(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name.capitalize()} cannot be empty")
        return v

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # To allow ORM objects to be serialized properly

# Initialize FastAPI App
app = FastAPI()

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "running", "service": "User Management API"}

@app.post("/users/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: UserSchema):
    db = SessionLocal()
    try:
        # Check for existing user with the same email
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="This email is already registered.")
        
        # Create new user
        new_user = User(name=user.name, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()

@app.get("/users/", response_model=List[UserResponseSchema], tags=["Users"])
def get_users():
    db = SessionLocal()
    try:
        return db.query(User).all()
    finally:
        db.close()
