


def nthFibonaciNumber(n):
    if n<=0:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1

    return nthFibonaciNumber(n-1)+nthFibonaciNumber(n-2)

#print(nthFibonaciNumber(10))





def sumOfNFibonaciNumber(n):
    if n<=0:
        return -1
    if n == 1:
        return 0
    if n==2:
        return 1
    first , second = 0 , 1
    result = first + second
    for i in range(0,n-2):
        next = first + second
        result+=next
        first = second
        second = next
    print(result)

#sumOfNFibonaciNumber(10)



arr = [1,2,1,2,1,2,3,4,5,3,4,5,6,7]
my_set = set(arr)

#for ele in my_set:
    #print(ele,end=" ")


my_set.add(34) # add 34 to the my_set

my_set.clear() # clear all the values of my_set

my_set.copy() # return a copy of set


# This is a dictionary


my_dict = {
    "name":"sudhanshu",
    "age":24,
    "Occupation":"Developer"
}


#print(type(my_dict))
#print(my_dict["name"])
my_dict["name"] = "sudhanshu kumar"
#print(my_dict["name"])

updated_name = {
    "name":"Twenkel sen"
}
my_dict.update(updated_name)
print(my_dict["name"])










#This is a dummy comment

class Car:
    engineType = "strongest Engine"
    numberOfTyers = 4
    numberOfWindow = 6
    isFridgeAValble = True


    def getNumberOfWindows(self):
        return self.numberOfWindow

    def getNumberOfTyres(self):
        return self.numberOfTyers

car1 = Car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())
















#This is a dummy comment
