from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users():
    return [{"user_id": 1, "name": "John Doe"}]
