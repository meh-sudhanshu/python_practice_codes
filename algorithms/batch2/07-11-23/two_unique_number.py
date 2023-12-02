


def getBothUniqueNumber(arr):
    ansXor = 0
    for e in arr: ansXor = ansXor^e
    pos = getFirstSetBitPosition(ansXor)
    segment1 = []
    segment2 = []
    ans1,ans2 = 0,0
    for e in arr:
        if isIthBitIsSet(e,pos) == True:
            ans1 = ans1^e
        else:
            ans2 = ans2^e
    return ans1,ans2

def getFirstSetBitPosition(n):
    ans = 1
    while n % 2 !=1:
        n = n>>1
        ans+=1
    return ans





def isIthBitIsSet(n,i):
    return ((n>>(i-1))%2 == 1)


arr = [2,6,2,7,6,9,1,99,65,9,1,99]
print(getBothUniqueNumber(arr))
