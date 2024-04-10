def getFirstSetBitPos(num):
    if num == 0 : return -1
    ans = 1
    while num%2 != 1:
        num = num>>1
        ans+=1
    return ans
def checkIthBit(num, i):
    return (num>>(i-1))%2 == 1
def getBothUniqueNumber(arr):
    ans1, ans2 = 0,0
    wholeXor = 0
    for e in arr: wholeXor = wholeXor^e
    pos = getFirstSetBitPos(wholeXor)
    for e in arr:
        if checkIthBit(e,pos) == True:
            ans1 = ans1^e
        else:
            ans2 = ans2^e
    return ans1,ans2

def main():
    arr = [1,1,3,2,3,4,7,7,8,2]
    print(getBothUniqueNumber(arr))
main()
