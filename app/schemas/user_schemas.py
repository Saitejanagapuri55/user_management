from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    nickname: Optional[str] = None
    profile_pic_url: Optional[HttpUrl] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    nickname: Optional[str] = None
    profile_pic_url: Optional[HttpUrl] = None

class UserResponse(UserBase):
    id: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "nickname": "johndoe",
                "profile_pic_url": "http://example.com/image.jpg"
            }
        }
    }
