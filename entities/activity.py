class Activity():
    def __init__(self, description, id=0):
        self.__description = description
        self.__id = id

    def getID(self):
        return self.__id
    
    def getDescription(self):
        return self.__description
    
    def __str__(self):
        return f"ID: {self.__id} - Description: {self.__description}"