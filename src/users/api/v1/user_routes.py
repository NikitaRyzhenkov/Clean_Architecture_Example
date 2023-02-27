from fastapi import APIRouter, HTTPException, status

from users.application.interactors.user import UserInteractor
from users.application.interfaces.schemas import UserCreate, UserResponse
from users.infrastructure.dependencies import (
    get_user_interactor,
    get_user_repository,
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
)
async def register(user_create: UserCreate) -> UserResponse:
    user_interactor: UserInteractor = get_user_interactor(get_user_repository())
    user = user_interactor.create_user(user_create)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
        )
    return UserResponse(**user.dict())


@router.post(
    "/login",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
)
async def login(username: str, password: str) -> UserResponse:
    user_interactor: UserInteractor = get_user_interactor(get_user_repository())
    user = user_interactor.authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return UserResponse(**user.dict())
