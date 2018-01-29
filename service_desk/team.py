from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base

team_analyst_association = Table('team_analyst', Base.metadata,
                                 Column('team_id', Integer,
                                        ForeignKey('team.id')),
                                 Column('analyst_id', Integer,
                                        ForeignKey('analyst.id')))


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    analysts = relationship('Analyst', secondary=team_analyst_association)

    def __init__(self, name):
        self.name = name
