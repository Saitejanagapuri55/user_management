from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User

class UserService:
    @staticmethod
    async def get_by_id(db_session: AsyncSession, user_id: int):
        result = await db_session.execute(select(User).filter_by(id=user_id))
        return result.scalars().first()

    @staticmethod
    async def get_by_email(db_session: AsyncSession, email: str):
        result = await db_session.execute(select(User).filter_by(email=email))
        return result.scalars().first()

    @staticmethod
    async def delete(db_session: AsyncSession, user_id: int):
        user = await UserService.get_by_id(db_session, user_id)
        if user:
            await db_session.delete(user)
            await db_session.commit()
            return True
        return False

    @staticmethod
    async def unlock_user_account(db_session: AsyncSession, user_id: int):
        user = await UserService.get_by_id(db_session, user_id)
        if user:
            user.is_locked = False
            await db_session.commit()
            return True
        return False

    @staticmethod
    async def create(db_session: AsyncSession, user_data: dict):
        user = User(**user_data)
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        return user
