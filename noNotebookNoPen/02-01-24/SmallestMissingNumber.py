

def fingSmallestMissingNumber(arr):
    arr.sort()
    if arr[0] != 0:
        return 0
    for i in range(len(arr)):
        if i == len(arr)-1:
            return arr[i]
        if arr[i+1] != arr[i]+1:
            return arr[i]+1
