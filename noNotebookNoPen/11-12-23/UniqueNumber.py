

def getUniqueNumber(arr):
    ans = 0
    for e in arr:
        ans = ans^e
    return ans

arr = [2,2,3,4,3]
print(getUniqueNumber(arr))