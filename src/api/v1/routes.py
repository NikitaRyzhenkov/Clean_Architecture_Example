from fastapi import APIRouter

from users.api.v1.user_routes import router as users_router

router = APIRouter()


@router.get("/")
async def main_route():
    return {"message": "It is alive!"}


router.include_router(users_router, prefix="/users")
