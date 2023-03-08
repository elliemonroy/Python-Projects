# Created Parent class 
class Parent:
    fname = "bob"
    lname = "jones"
    email = "bobjones@yahoo.com"
    password = "3332"
    

    # Created a function to get information from parent
    def getInfo(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_info = input("Enter your email address: ")
        password_info = input("Enter your password: ")
        if (email_info == self.email and password_info == self.password):
            print("Welcome back, {} {}!".format(first_name,last_name))
        else:
            print("The password or email is incorrect. Try again!")
    

# Created child class Student 
class Student(Parent):
    fname = "kelly"
    lname = "rogers"
    Grade = 11
    email = "kr23@gmail.com"
    studentID = "1221"

    # Created a function to get information from Student
    def getInfo(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_info = input("Enter your email address: ")
        student_info = input("Enter your student ID: ")
        if (email_info == self.email and student_info == self.studentID):
            print("Welcome back, {} {}!".format(first_name,last_name))
        else:
            print("Email or Student ID is incorrect. Try again!")


# Created another child class Teacher
class Teacher(Parent):
    fname = "shelly"
    lname = "kane"
    Subject = "math"
    licenceNum = "1112"

    # Created a function to get information from Teacher
    def getInfo(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_info = input("Enter your email address: ")
        licence_info = input("Enter your licence number: ")
        if (email_info == self.email and licence_info == self.licenceNum):
            print("Welcome back, {} {}!".format(first_name,last_name))
        else:
            print("Email or licence number is incorrect. Try again!")





# Controlling the program flow
if __name__ == "__main__":
    # This code invokes the methods inside each class for Parent, Student, & Teacher.
    guardian = Parent()
    guardian.getInfo()

    minor = Student()
    minor.getInfo()

    educator = Teacher()
    educator.getInfo()

    
