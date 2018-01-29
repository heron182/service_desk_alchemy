from datetime import datetime

import pytest

from .analyst import Analyst
from .base import Base, Session, engine
from .problem import Problem


@pytest.fixture(scope='module')
def session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()


def test_can_save_analyst_to_db(session):
    analyst = Analyst('Heron')
    session.add(analyst)
    assert analyst == session.query(Analyst).first()


def test_can_save_problem_to_db(session):
    analyst = Analyst('Heron')
    problem = Problem(
        description='Some nasty problem',
        date_added=datetime.now(),
        analyst=analyst)
    session.add(problem)
    assert problem == session.query(Problem).first()
