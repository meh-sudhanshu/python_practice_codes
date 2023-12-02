


def findBothUniqueNumbers(arr):
    ansXor = 0
    segment1 = []
    segment2 = []
    for e in arr: ansXor = ansXor^e
    position = getFirstSetBitPosition(ansXor)
    for e in arr:
        if isIthBitSet(e,position) == True:
            segment1.append(e)
        else:
            segment2.append(e)
    print(segment1)
    print(segment2)

def getFirstSetBitPosition(n):
    ans = 1
    while n%2 == 0:
        n = n>>1
        ans+=1
    return ans

def isIthBitSet(n,i):
    return (n>>(i-1) % 2 == 1)


arr = [2,3,5,2,5,7,15,17,15,34,17]
findBothUniqueNumbers(arr)



