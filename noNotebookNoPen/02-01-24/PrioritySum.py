

def prioritySum(arr,priorityArray):
    arr.sort()
    priority = 1
    ans = 0
    for i in range(len(arr)-1,0,-1):
        if priority in priorityArray:
            ans+=arr[i]
        if arr[i] != arr[i-1]:
            priority+=1
    return ans