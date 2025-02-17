from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    hashed_password: str
    disabled: bool | None = None


class UserInDb(User):
    hashed_password = str


class UserAuth(BaseModel):
    username: str
    password: str





class SongBase(BaseModel):
    title: str
    description: str


class SongCreate(SongBase):
    pass


class SongUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]


class SongResponse(SongBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True


