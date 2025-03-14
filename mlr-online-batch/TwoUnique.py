
def getFirstSetBitPos(num):
    ans = 1
    while num%2 != 1:
        num = num >> 1
        ans+=1
    return ans
def getIthBit(n,i):
    n = n>>(i-1)
    if n%2 == 0:
        return 0
    else:
        return 1


def getAnsByXor(arr):
    wholeXor = 0
    for e in arr: wholeXor = wholeXor ^ e
    pos = getFirstSetBitPos(wholeXor)
    ans1, ans2 = 0, 0
    for e in arr:
        if getIthBit(e,pos) == 1:
            ans1 = ans1 ^ e
        else:
            ans2 = ans2 ^ e
    return ans1,ans2






def main():
    arr = {2,7,2,17,3,3,6,6}
    ans = getAnsByXor(arr)
    print(ans)

main()