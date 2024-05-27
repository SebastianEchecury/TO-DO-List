from entities import activity as act, person as per
from data import dbHandler
import os
clear = lambda: os.system('cls')
import datetime
import os

class Menu():

    def start(self):
        op = 0
        while op != 8:
            while op not in range(1, 9):
                self.showOptions()
                op = int(input('Enter option: '))
            if op == 8:
                break
            if op == 1:
                self.insertActivity()
            if op == 2:
                self.updateActivity()
            if op == 3:
                self.deleteActivity()
            if op == 4:
                self.assignActivity()
            if op == 5:
                self.markAsDone()
            if op == 6:
                self.markAsUndone()
            if op == 7:
                self.listActivities()
            op = 0

    def showOptions(self):
        print('1. Create Activity')
        print('2. Update Activity')
        print('3. Delete Activity')
        print('4. Assign Activity')
        print('5. Done Activity')
        print('6. Undone Activity')
        print('7. List Activities')
        print('8. Exit')

    def insertActivity(self):
        clear()
        desc = input('Enter description: ')
        a = act.Activity(desc)
        db = dbHandler.DbHandler()
        db.insertActivity(a)
        print('Activity successfully created')

    def updateActivity(self):
        clear()
        db = dbHandler.DbHandler()
        activities = db.getActivities()
        for a in activities:
            print(a)
        id = int(input('Enter activity id: '))
        newDescription = input('Enter new description: ')
        db.updateActivityDesc(id, newDescription)
        print('Activity successfully updated')

    def deleteActivity(self):
        clear()
        db = dbHandler.DbHandler()
        activities = db.getActivities()
        for a in activities:
            print(a)
        id = int(input('Enter activity id: '))
        if db.isItAssigned(id):
            print('Cant be deleted. Its already assigned')
        else:
            db.deleteActivity(id)
            print('Activity deleted')

    def assignActivity(self):
        clear()
        db = dbHandler.DbHandler()
        activities = db.getActivities()
        print('Activities')
        for a in activities:
            print(a)
        print()
        print('Persons')
        persons = db.getPersons()
        for p in persons:
            print(p)
        print()
        idActivity = int(input('Enter Activity ID: '))
        idPerson = int(input('Enter Person ID: '))
        op = input('Add expiring date? y/n: ')
        expiringDate = ''
        if op == 'y':
            expiringDate = input('Enter expiring date (yyyy-mm-dd): ')

        db.assignActivityPerson(idActivity, idPerson, expiringDate)
        print('Activity assigned')

    def markAsDone(self):
        clear()
        db = dbHandler.DbHandler()
        persons = db.getPersons()
        for p in persons:
            print(p)
        print()
        idPerson = int(input('Enter id of the person to mark activity as done: '))

        activities = db.getActivitiesByPerson(idPerson, False)
        if not activities:
            print('There is no pending activities')
        else:
            print('Activities')
            for a in activities:
                print(a)
            print()
            idAP = int(input('Enter Activity ID: '))
            db.setDone(idAP, True)
            print('Activity marked as done')
    
    def markAsUndone(self):
        clear()
        db = dbHandler.DbHandler()
        persons = db.getPersons()
        for p in persons:
            print(p)
        print()
        idPerson = int(input('Enter id of the person to mark activity as done: '))

        activities = db.getActivitiesByPerson(idPerson, True)
        if not activities:
            print('There is no finished activities')
        else:
            print('Activities')
            for a in activities:
                print(a)
            print()
            idAP = int(input('Enter Activity ID: '))
            db.setDone(idAP, False)
            print('Activity marked as undone')

    def listActivities(self):
        f = self.createFile()
        db = dbHandler.DbHandler()
        persons = db.getPersons()
        f.write('TO-DO List \n\n')
        for p in persons:
            f.write(f'ID: {p.getID()}.{p.getLastName()}, {p.getName()}\n')
            f.write('Not Done\n')
            activities = db.getActivitiesByPerson(p.getID(), False)
            if not activities:
                f.write('No pending activities\n')
            else:
                for a in activities:
                    f.write(f'ID: {a.getID()} - {a.getDescription()}\n')
            f.write('Done\n')
            activities = db.getActivitiesByPerson(p.getID(), True)
            if not activities:
                f.write('No finished activities\n')
            else:
                for a in activities:
                    f.write(f'ID: {a.getID()} - {a.getDescription()}\n')
            f.write('\n\n')

    def createFile(self):
        today = datetime.date.today()
        dateFormat = "%d-%m-%Y"
        sToday = today.strftime(dateFormat)
        path = os.path.abspath(__file__)
        fileName = os.path.dirname(path) + '\\' + sToday + '.txt'
        f = open(fileName, 'w+')
        return f
