
import random
from db import engine, db_session, Base
from employee.models import Employee
from department.models import Department


Base.metadata.create_all(bind=engine)

departments = [Department(name='Engineering'), Department(name='Human Resources'), Department(name='Marketing')]

for department in departments:
    db_session.add(department)


employees = ['Fede', 'Peter', 'Roy', 'Tracy', 'Bill', 'Joe', 'Dude', 'Alex']

for employee in employees:
    db_session.add(Employee(name=employee, department=random.choice(departments)))
db_session.commit()