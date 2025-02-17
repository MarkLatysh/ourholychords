from sqlalchemy import Column, String
from database.base import BASE


class Song(BASE):
    __tablename__ = "songs"

    id = Column(String, nullable=False)
    name = Column(String, min_lenght=1, max_lenght=30, nullable=False)
    text = Column(String, nullable=False)

    def __str__(self):
        return f"{self.name} - {self.description}"