


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

sumOfNFibonaciNumber(10)

















#This is a dummy comment
