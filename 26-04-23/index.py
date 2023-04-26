



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
    def getName(self):
        return "parent1"
class Parent2:
    def defName():
        return "Parent2"
class Parent3:
    def getName():
        return "Parent 3"

class Child(Parent1 , Parent2 , Parent3):
    def __init__(self):
        self.getAllParent()
    def getAllParent(self):
        print("trying to get all parents of this class")
        parent_list = []
        for base in Child.__bases__:
            parent_list.append(base)
        print(parent_list)
#my_child = Child()
#parent_list = []
#print(my_child.__bases__)
#for base in Child.__bases__:
    #print(base,end=" ")

#print(my_child.getName())


#print("sudhanshu","Kumar","nityanand","singh")
#print("sudhansu")


def addNumbers(a,b):
    print(a+b)

def addNumbers2(*args):
    sum = 0
    for value in args:
        sum+=value
    print(sum)

#addNumbers2(10)
#addNumbers2(10,20)

#addNumbers2(10,20)
#addNumbers2(10,20,30)


# def addNumbers3(arg1 , arg2 , *arg3):
#     print(arg1,arg2,arg3)

#addNumbers3(10,20,30)
#addNumbers3(10,20,30,40,50,60)


def addNumbers(a,b,c=2):
    print(a+b+c)

#addNumbers(10,20)
#addNumbers(10,20,30)


#def doJob(agr1,agr2,agr3):
    print("sudhanshu")

#def doJob(arg1):
    #print("sudhanshu kumar nityanand singh")

#doJob(10)
#oJob(10,20,30)

class Animal:
    def printSomething(self):
        print("Animals are good by nature")
    def canFly(self,name):
        if(name == "tarak"):
            print("animal tarak can fly")
        else:
            print("no animals can fly")
class Dog(Animal):
    def canFly(self):
        print("dogs can not fly")
class Tarak(Animal):
    def canFly(self):
        print("tarak can fly")
#my_tarak.canFly()















# This is a dummy comment
