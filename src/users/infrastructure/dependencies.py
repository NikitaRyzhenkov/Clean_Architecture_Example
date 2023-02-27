from users.application.interactors.user import UserInteractor
from users.application.interfaces.user import UserInterface
from users.infrastructure.repositories.user import InMemoryUserRepository


def get_user_repository() -> UserInterface:
    return InMemoryUserRepository()


def get_user_interactor(user_repository: UserInterface) -> UserInteractor:
    return UserInteractor(user_repository)
