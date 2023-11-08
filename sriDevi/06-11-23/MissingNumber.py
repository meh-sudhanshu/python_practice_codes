def missingNumber(arr,n):
    ans = 0
    for i in range(1,n+1): ans = ans^i
    for e in arr: ans = ans^e
    return ans

n = 10
arr = [2,1,3,6,7,4,9,10,8]

print(missingNumber(arr,n))


# print(type(missingNumber))
