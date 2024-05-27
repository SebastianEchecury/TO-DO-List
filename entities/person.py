class Person():
    def __init__(self, name, lastName, birthDate, id=0):
        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__birthDate = birthDate

    def getName(self):
        return self.__name
    
    def getLastName(self):
        return self.__lastName
    
    def getBirthDate(self):
        return self.__birthDate
    
    def getID(self):
        return self.__id
    
    def __str__(self):
        return f"ID: {self.getID()} - Name: {self.getName()} - Last Name: {self.getLastName()} - Birth Date: {self.getBirthDate()}"