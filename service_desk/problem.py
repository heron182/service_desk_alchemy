from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date_added = Column(Date)
    analyst_id = Column(Integer, ForeignKey('analyst.id'))
    analyst = relationship('Analyst', backref='problems')

    def __init__(self, description, date_added, analyst):
        self.description = description
        self.date_added = date_added
        self.analyst = analyst

    def __repr__(self):
        return f'ID: {self.id} - {self.description}'
