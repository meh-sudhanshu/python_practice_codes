
def getMissingNumber(arr,n):
    result = 0
    for i in range(1,n+1): result = result ^ i
    for e in arr: result = result ^ e

    return result


arr = [1,4,2,3,5,8,6]
n = 8

print(getMissingNumber(arr,n))