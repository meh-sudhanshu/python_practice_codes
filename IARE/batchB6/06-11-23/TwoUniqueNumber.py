def getBothUniqueNumber(arr):
    ansXor = 0
    for e in arr: ansXor = ansXor ^ e
    pos = getFirstSetBitPosition(ansXor)
    ans1 , ans2 = 0, 0
    for e in arr:
        if isIthBitSet(e,pos) == True:
            ans1 = ans1 ^ e
        else:
            ans2 = ans2 ^e
    return ans1, ans2

def isIthBitSet(n,i):
    return ((n>>(i-1)) %2 == 1)


def getFirstSetBitPosition(n):
    pos = 1
    while n%2 != 1:
        n = n>>1
        pos+=1
    return pos


arr = [2,4,2,6,4,7,14,15,15,17,6,17]
print(getBothUniqueNumber(arr))