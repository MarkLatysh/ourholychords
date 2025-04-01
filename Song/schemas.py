from pydantic import BaseModel
from typing import Optional



class SongBase(BaseModel):
    id: int
    name: str
    text: str


class SongCreate(SongBase):
    id: int
    name: str
    text: str


class SongUpdate(BaseModel):
    id: Optional[int]
    name: Optional[str]
    text: Optional[str]


class SongResponse(SongBase):
    id: int
    name: str
    text: str

    class Config:
        orm_mode = True


