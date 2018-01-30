from service_desk import Analyst, Problem, Session, Team, Ticket

session = Session()

print('Listing all teams and analysts associated')
for team in session.query(Team).all():
    print(f'{team.name} - Analysts: {team.analysts}')

print('\nListing all problems created by Sam')
for problem in session.query(Problem).join(
        Analyst, Problem.analyst).filter(Analyst.name == 'Sam').all():
    print(f'{problem}')

print('\nListing all tickets closed by John')
john = session.query(Analyst).filter(Analyst.name == 'John').one()
for ticket in session.query(Ticket).filter(Ticket.analyst == john).all():
    print(f'{ticket}')

session.close()
