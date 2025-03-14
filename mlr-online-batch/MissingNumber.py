def getMissingNumberByMath(n,arr):
    ans = (n*(n+1)//2) - sum(arr)
    return int(ans)

def getMissingNumberByDictionary(n,arr):
    _dict = {}
    for e in arr:
        _dict[e] = 1
    for i in range(1,n+1):
        if i not in _dict:
            return i
        
def getMissingNumberByXor(n,arr):    
    ans = 0
    for i in range(1,n+1): ans = ans^i
    for e in arr: ans = ans^e
    return ans




def main():
    n = 6
    arr = [1,6,5,3,2]
    ans1 = getMissingNumberByMath(n,arr)
    ans2 = getMissingNumberByDictionary(n,arr)
    ans3 = getMissingNumberByXor(n,arr)
    print(ans1,ans2,ans3)

main()