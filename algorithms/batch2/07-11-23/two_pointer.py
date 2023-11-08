


def getOrDeafaultPairs(arr,target):
    arr.sort()
    i,j = 0, len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] < target: i+=1
        if arr[i]+arr[j] > target: j-=1

    return False

arr = [2,5,-3,65,23]
target = 200 
print(getOrDeafaultPairs(arr,target))