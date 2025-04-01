from sqlalchemy import Column, String, Integer
from database.base import BASE


class Song(BASE):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __str__(self):
        return f"{self.id} - {self.name}"