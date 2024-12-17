from app.schemas.user_schemas import UserCreate, UserUpdate
from app.utils.security import hash_password, verify_password

class UserService:
    def create_user(self, user_data: UserCreate):
        """
        Create a new user with hashed password.
        """
        hashed_password = hash_password(user_data.password)
        return {
            "email": user_data.email,
            "name": user_data.name,
            "nickname": user_data.nickname,
            "profile_pic_url": user_data.profile_pic_url,
            "hashed_password": hashed_password,
        }

    def update_user(self, user_data: UserUpdate):
        """
        Update user details based on provided fields.
        """
        updated_data = user_data.dict(exclude_unset=True)
        return updated_data

    def verify_user_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against a hashed password.
        """
        return verify_password(plain_password, hashed_password)
