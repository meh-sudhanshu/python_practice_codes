def getMaximumWindowSum(arr,ws):
    ans = float('-inf')
    i , j = 0 , ws-1
    ps = 0
    while j < len(arr):
        if i == 0:
            sum = 0
            for k in range(i,j+1):
                sum+=arr[k]
            
        else:
            sum = ps - arr[i-1]+arr[j]
        ans = max(ans,sum)
        ps = sum
        i+=1
        j+=1
    return ans

arr = [1,4,2,-7,3,5,2]
ws = 3
print(getMaximumWindowSum(arr,ws))