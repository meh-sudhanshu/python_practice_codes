
def getFirstSetBitPosition(num):
    ans = 1
    while num%2 != 1:
        num = num>>1
        ans+=1
    return ans


def getIthBit(num,i):
    return True if (((num>>(i-1))%2 == 1)) else False

def getBothUniqueNumber(arr):
    allXor = 0
    for e in arr: allXor = allXor ^ e

    firstSetBit = getFirstSetBitPosition(allXor)
    ans1, ans2 = 0, 0

    for e in arr:
        if getIthBit(e,firstSetBit) == True:
            ans1 = ans1 ^e
        else:
            ans2 = ans2^e
    return ans1, ans2



def main():
    arr = [2,3,7,3,7,9]
    ans = getBothUniqueNumber(arr)
    print(ans)

main()