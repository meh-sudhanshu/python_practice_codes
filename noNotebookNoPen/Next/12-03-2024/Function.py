# def getSum(a,b):
#     return a+b

def greaterOfThree(a,b,c):
    return a if a>b and a>c else b if b>a and b>c else c
# print(greaterOfThree(1,2,3))
# addTwoNumbers = lambda(a,b):a+b


#  def main():
#     ans = getSum(20,30)
#     print(ans)

# main()

def addNumbers(*args):
    sum_ = 0
    for num in args:
        sum_+=num
    print(sum_)

def printObject(**kargs):
    print(kargs)

printObject(name="sudhanshu",height="5ft7inch")

addNumbers(1,2,3)