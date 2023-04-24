
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
print(output)
