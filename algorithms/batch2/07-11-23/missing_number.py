

def missingNumber(arr,n):
    ans = 0
    for i in range(1,n+1): ans = ans^i
    for e in arr: ans = ans^e
    return ans

arr = [1,7,8,3,5,2,4]
n = 8
print(missingNumber(arr,n))