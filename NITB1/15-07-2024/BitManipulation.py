

def getFirstSetBitPosition(n):
    ans = 1
    while n%2 != 1:
        n = n>>1
        ans+=1
    return ans

def getIthBit(n,i):
    return int((n>>(i-1))% 2 == 1)
    
def main():
    n  = int(input())
    i = int(input())
    #ans = getFirstSetBitPosition(n)
    ans = getIthBit(n,i)
    print(ans)

main()