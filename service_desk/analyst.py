from sqlalchemy import Column, Integer, String

from .base import Base


class Analyst(Base):
    __tablename__ = 'analyst'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
