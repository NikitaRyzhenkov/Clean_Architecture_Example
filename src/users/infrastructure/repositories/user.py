from users.application.entities.user import User
from users.application.interfaces.schemas import UserCreate
from users.application.interfaces.user import UserInterface


class InMemoryUserRepository(UserInterface):
    users: dict[int, User] = {}

    def get_all_users(self) -> list[User]:
        return list(self.users.values())

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def get_user_by_username(self, username: str) -> User | None:
        mapper = {i.username: i_id for i_id, i in self.users.items()}
        return self.users.get(mapper.get(username))

    def create_user(self, user: UserCreate) -> User:
        usernames = {i.username for i in self.users.values()}
        if user.username not in usernames:
            next_id = max(self.users.keys()) + 1 if self.users else 0
            user = User(**user.dict(), id=next_id)
            self.users[user.id] = user
            next_id += 1
            return user

    def update_user(self, user_id: int, user: User) -> User:
        db_user = self.users.get(user_id)
        if db_user:
            self.users[user_id] = user
            return self.users[user_id]

    def delete_user(self, user_id: int) -> None:
        self.users.pop(user_id, None)
