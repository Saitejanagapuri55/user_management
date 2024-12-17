from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app.models.user_model import User
from pydantic import BaseModel, EmailStr
from sqlalchemy.exc import SQLAlchemyError
from app.models.user_model import Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="User Management System",
    description="A robust User Management API built with FastAPI and PostgreSQL.",
    version="1.0.0",
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "running", "service": "User Management API"}

# Create user endpoint
@app.post("/users/", tags=["Users"])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Validate inputs
    if not user.name.strip() or not user.email.strip() or not user.password.strip():
        raise HTTPException(status_code=400, detail="Fields cannot be empty")
    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters long.")

    # Check for duplicate email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="This email is already registered.")

    # Create new user
    try:
        new_user = User(name=user.name, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error occurred.")

# Retrieve all users
@app.get("/users/", tags=["Users"])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
