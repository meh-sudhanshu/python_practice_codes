



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
    def getParentName():
        return "parent1"

class Parent2:
    def defParentName():
        return "Parent2"
class Parent3:
    def getParentName():
        return "Parent 3"

class Child(Parent1 , Parent2 , Parent3):
    def getAllParent():
        #write custom logic here to get all parents name






















# This is a dummy comment
