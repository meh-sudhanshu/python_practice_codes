def isPairExist(arr,target):
    arr.sort()
    i,j = 0,len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] < target: i+=1
        if arr[i]+arr[j] > target: j-=1
    return False
    
arr = [-3,6,7,12,13,-89,34,54,76,58]
target = 1100
print(isPairExist(arr,target))
