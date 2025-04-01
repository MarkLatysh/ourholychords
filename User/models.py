from sqlalchemy import Column, String, Integer
from database.base import BASE


class User(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    def __str__(self):
        return f"{self.id} - {self.username}"