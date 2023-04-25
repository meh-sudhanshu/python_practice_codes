
def add():
    try:
        a = int(input())
    except ValueError as err:
        print(err)
    try:
        b = int(input())
    except ValueError as err:
        print(err)
    print(a+b)


#add()

def addNumbers():
    a = 10
    b = 20
    return (a+b)


sum = addNumbers()
#print(sum)


def addNumber(a,b):
    return a+b


sum = addNumber(10,30)



def returningMultipleValues():
    return 10,20,30

output = returningMultipleValues()
#print(output)




def printFibonaciSequence(n):
    if n<=0:
        print("invalid argument")
        return -1
    if n==1:
        print(0)
        return -1
    if n==2:
        print(0," ",1)
        return -1
    a = 0
    b = 1
    print(a," ",b)
    count = 3
    while count <=n:
        next = a+b
        print(next , end = " ")
        a = b
        b= next
        count+=1
#printFibonaciSequence(10)


def findLcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b

    while True:
        if((greater % a == 0) and (greater%b) == 0):
            lcm = greater
            break
        greater+=1
    return lcm

#print(findLcm(18,20))





def doJob(n):
    if n<=2:
        return
    print(n)
    doJob(n-1)
    print(n)


#doJob(10)



def doJob2(n):
    if n<=5:
        return
    doJob2(n-1)
    print(n,end=" ")
    doJob2(n-1)
    print(n,end=" ")
#doJob2(8)



def printSteps(source,helper,destination,n):
    if n<=0:
        return
    print(source,"to",helper)
    printSteps(source,)



















#this is a dummy comment


















#This is a dummy comment



















#This is a dummy comment
