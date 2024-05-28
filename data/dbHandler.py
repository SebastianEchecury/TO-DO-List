import psycopg2
from entities import person as pe
from entities import activity as act

class DbHandler():
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'postgres'
        self.password = '1234'
        self.database = 'TODOList'

    def getConnection(self, conn):
        try:
            conn = psycopg2.connect(
                dbname = self.database,
                user = self.username,
                password = self.password,
                host = self.hostname
            )
        except Exception as e:
            print(f"Error: {e}")
        
        return conn
    
    def closeConnection(self, conn):
        conn.close()

    def insertPerson(self, p:pe.Person):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        INSERT INTO Person (name, lastName, birthDate, role, password)
        VALUES ('{p.getName()}', '{p.getLastName()}', '{p.getBirthDate()}', '{p.getRole()}', '{p.getPassword()}')
        '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def insertActivity(self, a:act.Activity):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        INSERT INTO Activity (description)
        VALUES ('{a.getDescription()}')
        '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def getActivities(self):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        SELECT *
        FROM Activity
        '''
        cursor.execute(query)
        aux = cursor.fetchall()
        activities = list()
        for a in aux:
            a1 = (act.Activity(a[1], a[0]))
            activities.append(a1)
        self.closeConnection(conn)
        return activities
    
    def updateActivityDesc(self, id, newDescription):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        UPDATE Activity
        SET description = '{newDescription}'
        WHERE id = {id}
        '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def isItAssigned(self, id):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        SELECT *
        FROM Activity A
        JOIN PersonActivity PA
	    ON A.id = PA.idActivity
        WHERE A.id = {id}
        '''
        cursor.execute(query)
        aux = cursor.fetchall()
        self.closeConnection(conn)
        if not aux:
            return False
        else:
            return True
        
    def deleteActivity(self, id):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        DELETE FROM Activity
        WHERE id = {id}
        '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def getPersons(self):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
        SELECT *
        FROM Person
        '''
        cursor.execute(query)
        aux = cursor.fetchall()
        persons = list()
        for p in aux:
            p1 = (pe.Person(p[1], p[2], p[3], p[4], p[5], p[0]))
            persons.append(p1)
        self.closeConnection(conn)
        return persons
    
    def assignActivityPerson(self, idActivity, idPerson, expiringDate):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        if expiringDate == '':
            query = f'''
            INSERT INTO 
            PersonActivity(idperson, idactivity)
            VALUES ({idPerson}, {idActivity})
            '''
        else:
            query = f'''
            INSERT INTO 
            PersonActivity(idperson, idactivity, expiringDate)
            VALUES ({idPerson}, {idActivity}, '{expiringDate}')
            '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def getActivitiesByPerson(self, idPerson, done):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
            SELECT PA.id, A.description, PA.expiringDate
            FROM Activity A
            JOIN PersonActivity PA
	        ON A.id = PA.idActivity
	        AND PA.idPerson = {idPerson}
	        AND PA.done IS {done}
            '''
        cursor.execute(query)
        aux = cursor.fetchall()
        activities = list()
        for a in aux:
            a1 = (act.Activity(a[1], a[0]))
            activities.append(a1)
        self.closeConnection(conn)
        return activities
        
    def setDone(self, idAP, done):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
            UPDATE PersonActivity
            SET done = {done}
            WHERE id = {idAP}
            '''
        cursor.execute(query)
        conn.commit()
        self.closeConnection(conn)

    def getPersonByID(self, id):
        conn = ''
        conn = self.getConnection(conn)
        cursor = conn.cursor()
        query = f'''
            SELECT * 
            FROM Person
            WHERE id = {id}
            '''
        cursor.execute(query)
        aux = cursor.fetchone()
        p = ''
        if not aux:
            return False
        else:
            p = pe.Person(aux[1], aux[2], aux[3], aux[4], aux[5], aux[0])
        self.closeConnection(conn)
        return p