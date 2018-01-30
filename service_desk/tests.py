from datetime import datetime

import pytest

from .analyst import Analyst
from .base import Base, Session, engine
from .problem import Problem
from .ticket import Ticket
from .team import Team


@pytest.fixture(scope='module')
def session():
    Base.metadata.create_all()
    session = Session()
    yield session
    session.commit()
    session.close()
    Base.metadata.drop_all()


def test_can_save_analyst_to_db(session):
    analyst = Analyst('Heron')
    session.add(analyst)
    assert analyst == session.query(Analyst).first()


def test_can_save_team_to_db(session):
    team = Team(name='Super Team ZY')
    session.add(team)
    assert team == session.query(Team).first()


def test_can_associate_analyst_to_team(session):
    team = session.query(Team).first()
    team.analysts = [
        session.query(Analyst).first(),
    ]
    assert team.analysts.pop() == session.query(Analyst).first()


def test_can_save_problem_to_db(session):
    analyst = session.query(Analyst).first()
    problem = Problem(
        description='Some nasty problem',
        date_added=datetime.now(),
        analyst=analyst)
    session.add(problem)
    assert problem == session.query(Problem).first()


def test_can_save_new_ticket_to_db(session):
    ticket = Ticket(description='Some general problem on my system')
    session.add(ticket)
    assert ticket == session.query(Ticket).first()


def test_can_save_solved_ticket_to_db(session):
    ticket = session.query(Ticket).first()
    analyst = session.query(Analyst).first()
    problem = session.query(Problem).first()
    ticket.analyst = analyst
    ticket.problem = problem
    ticket.finished_at = datetime.now()
    assert ticket == session.query(Ticket).first()
