

def getFirstSetBitPosition(n):
    if n == 0:
        return -1
    ans = 1
    while n%2 != 1:
        n = n>>1
        ans+=1
    return ans

def getIthBit(n,i):
    return int((n>>(i-1))% 2 == 1)
    
def main():
    arr = [2,4,2,67,67,8,4,3,3,17]
    wholeXor = 0
    for e in arr : wholeXor = wholeXor^e
    firstPos = getFirstSetBitPosition(wholeXor)
    ans1 , ans2 = 0, 0
    for i in range(len(arr)):
        e = arr[i]
        if getIthBit(e,firstPos) == 1:
            ans1 = ans1^e
        else:
            ans2 = ans2^e
    print(ans1,ans2)
    

main()