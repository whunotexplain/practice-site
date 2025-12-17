from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user_demo_model import Users


def create_admin(user_in: Users) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }


def get_admin_by_id(id_user: int) -> dict:
    return {
        "success": True,
        "user": {
            "id": id_user,
            "login": f"user_{id_user}",
            "password": f"password_{id_user}",
        },
    }


async def get_admin_by_login(db: AsyncSession, login: str):
    """Получить пользователя по username"""
    result = await db.execute(select(Users).where(Users.login == login))
    return result.scalar_one_or_none()
