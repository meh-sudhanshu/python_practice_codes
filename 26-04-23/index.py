



class Book:
    numberOfPages = 145
    author = "sudhanshu"
    scope = "To be sold in india"

    def __init__(self , zone , dob):
        self.zone = zone
        self.dob = dob
    def __del__(self):
        print("destructor is called")

#my_book = Book("Mystery","25-10-1998")
#print(my_book.zone)
#print(my_book.dob)
#del my_book
#_------------------------------------------------------------_#

# OOPS PILLARS
class School:
    name = "RJSIS"
    age = 34
    #def __init__(self , age):
        #self.age = age
    def getAge(self):
        return self.age
class SubSchool(School):
    def __init__(self):
        print("child constructor")
    def getParentName(self):
        return "RJSIS"
    def getName(self):
        return "Gyan Sagar"

#my_school = SubSchool()
#print(my_school.getParentName())
#print(my_school.getName())
#print(my_school.getAge())

class Parent1:
    def getParentName(self):
        print("parent1")
        super(Parent1,self).getParentName()
class Parent2:
    def getParentName(self):
        print("Parent2")
        super(Parent2,self).getParentName()
class Parent3:
    def getParentName(self):
        print("Parent 3")
class Child(Parent1 , Parent2 , Parent3):
    def getAllParent(self):
        #write custom logic here to get all parents name
        super(Child, self).getParentName()
obj = Child()
obj.getParentName()























# This is a dummy comment
