from passlib.context import CryptContext

from users.application.entities.user import User
from users.application.interfaces.schemas import UserCreate
from users.application.interfaces.user import UserInterface

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserInteractor:
    def __init__(self, user_repository: UserInterface) -> None:
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> User:
        user.password = pwd_context.hash(user.password)
        return self.user_repository.create_user(user)

    def authenticate_user(self, username: str, password: str) -> User | None:
        user = self.user_repository.get_user_by_username(username)
        if not user:
            return None
        if not pwd_context.verify(password, user.password):
            return None
        return user

    def get_user_by_username(self, username: str) -> User:
        return self.user_repository.get_user_by_username(username)
