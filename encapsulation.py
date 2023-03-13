
#created a class Student
class Student: 
    def __init__(self):
        self._name = "bob" 
        self.__age = 22

    def getPrivate(self):
        print(self.__age)

    def setPrivate(self, private):
        self.__age = private



#calling Student class
obj = Student()
obj._name = "Jane"
print(obj._name)
obj.getPrivate()
obj.setPrivate(24)
obj.getPrivate()





    

        
    
