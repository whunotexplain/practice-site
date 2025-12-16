from .schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }


def get_user_by_id(id_user: int) -> dict:
    return {
        "success": True,
        "user": {
            "id": id_user,
            "login": f"user_{id_user}",
            "password": f"password_{id_user}",
        },
    }
