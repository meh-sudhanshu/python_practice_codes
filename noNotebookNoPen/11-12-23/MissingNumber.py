
def getMissingNumber(n,arr):
    ans = 0
    for i in range(1,n+1):
        ans = ans^i
    for e in arr:
        ans = ans^e
    return ans    



n = 10
arr = [1,4,3,2,6,7,8,9,10]

print(getMissingNumber(n,arr))