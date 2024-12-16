from fastapi import FastAPI
from app.routes import users
from app.db import init_db

app = FastAPI(title="User Management System")

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(users.router)
