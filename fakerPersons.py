from faker import Faker
from entities import person
from data import dbHandler
from datetime import datetime



f = Faker()
db = dbHandler.DbHandler()

for n in range(0, 10):
    name = f.name()
    birthDate = f.date_between(start_date=datetime.strptime('1950-01-01', '%Y-%m-%d').date(), end_date=datetime.strptime('2000-12-31', '%Y-%m-%d').date()) #yyyy-mm-dd
    aux = name.split(' ')

    p = person.Person(aux[0], aux[1], birthDate)
    db.insertPerson(p)