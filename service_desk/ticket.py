from datetime import datetime

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    finished_at = Column(Date, default=None)
    problem_id = Column(Integer, ForeignKey('problem.id'), nullable=True)
    problem = relationship('Problem', backref='tickets')
    analyst_id = Column(Integer, ForeignKey('analyst.id'), nullable=True)
    analyst = relationship('Analyst', backref='tickets')

    def __init__(self,
                 description,
                 finished_at=None,
                 problem=None,
                 analyst=None):
        self.description = description
        self.finished_at = finished_at
        self.problem = problem
        self.analyst = analyst

    def __repr__(self):
        return f'ID:{self.id} finished_at:{self.finished_at} by {self.analyst}'
