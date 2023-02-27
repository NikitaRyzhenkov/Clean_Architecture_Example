from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    password: str
    email: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
