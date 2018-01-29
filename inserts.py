from datetime import datetime

from service_desk.analyst import Analyst
from service_desk.base import Base, Session
from service_desk.problem import Problem
from service_desk.team import Team
from service_desk.ticket import Ticket

Base.metadata.create_all()
session = Session()

print('Inserting data...')

# analysts
a1 = Analyst(name='Sam')
a2 = Analyst(name='John')
a3 = Analyst(name='Chris')
a4 = Analyst(name='Mary')
a5 = Analyst(name='Louise')
a6 = Analyst(name='Elizabeth')
a7 = Analyst(name='Kurt')
a8 = Analyst(name='Mark')
a9 = Analyst(name='Molly')

session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9])

# teams
t1 = Team(name='Team A')
t2 = Team(name='Team B')
t3 = Team(name='Team C')
t4 = Team(name='Team D')
t5 = Team(name='Team E')

t1.analysts = [a1, a2, a3]
t2.analysts = [a4, a5, a6]
t3.analysts = [a7, a8, a9]
t4.analysts = [a1, a5, a6]
t5.analysts = [a3, a7, a9]

session.add_all([t1, t2, t3, t4, t5])

# problems
p1 = Problem(
    description='A bad problem', date_added=datetime.now(), analyst=a1)
p2 = Problem(
    description='A not so bad problem', date_added=datetime.now(), analyst=a4)
p3 = Problem(
    description='A big problem', date_added=datetime.now(), analyst=a4)
p4 = Problem(
    description='A small problem', date_added=datetime.now(), analyst=a4)
p5 = Problem(
    description='Just a problem', date_added=datetime.now(), analyst=a6)
p6 = Problem(
    description='Not sure if a problem', date_added=datetime.now(), analyst=a6)
p7 = Problem(
    description='That one was hard', date_added=datetime.now(), analyst=a8)
p8 = Problem(
    description='Extra time problem', date_added=datetime.now(), analyst=a8)
p9 = Problem(description='Fake problem', date_added=datetime.now(), analyst=a9)
p10 = Problem(
    description='No problem at all', date_added=datetime.now(), analyst=a2)

session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

#tickets
tk1 = Ticket(
    description='Can\'t open program a',
    finished_at=datetime.now(),
    analyst=a2,
    problem=p4)
tk2 = Ticket(
    description='Can\'t connect to network',
    finished_at=datetime.now(),
    analyst=a2,
    problem=p2)
tk3 = Ticket(
    description='Can\'t logon',
    finished_at=datetime.now(),
    analyst=a8,
    problem=p1)
tk4 = Ticket(
    description='Can\'t open program b',
    finished_at=datetime.now(),
    analyst=a2,
    problem=p4)
tk5 = Ticket(
    description='System is down',
    finished_at=datetime.now(),
    analyst=a8,
    problem=p8)
tk6 = Ticket(
    description='Mail app not working',
    finished_at=datetime.now(),
    analyst=a6,
    problem=p3)
tk7 = Ticket(
    description='Can\'t open program f',
    finished_at=datetime.now(),
    analyst=a7,
    problem=p4)
tk8 = Ticket(
    description='Caonnection problem',
    finished_at=datetime.now(),
    analyst=a5,
    problem=p1)
tk9 = Ticket(
    description='Can\'t open program a',
    finished_at=datetime.now(),
    analyst=a2,
    problem=p4)
tk10 = Ticket(
    description='Can\'t open program b',
    finished_at=datetime.now(),
    analyst=a9,
    problem=p7)

session.add_all([tk1, tk2, tk3, tk4, tk5, tk6, tk7, tk8, tk9, tk10])

session.commit()
session.close()