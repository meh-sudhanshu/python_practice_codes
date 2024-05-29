def getMissingNumber(n,arr):
    ans = 0
    for i in range(1,n+1):
        ans = ans^i
    for i in range(len(arr)):
        ans = ans^arr[i]
    return ans