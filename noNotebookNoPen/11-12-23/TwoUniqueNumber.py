def getFirstSetBitPosition(num):
    ans = 1
    while num%2 == 0:
        ans+=1
        num = num>>1
    return ans

def isIthBitSet(num,i):
    num = num>>(i-1)
    return num%2 == 1


def getBothUniqueNumber(arr):
    ans = 0
    ans1, ans2 = 0, 0
    for e in arr:
        ans = ans^e
    pos = getFirstSetBitPosition(ans)

    for e in arr:
        if isIthBitSet(e,pos) == True:
            ans1 = ans1^e
        else:
            ans2 = ans2^e
    print(ans1)
    print(ans2)





arr = [1,2,3,6,5,1,2,3,5,7]
getBothUniqueNumber(arr)