def getMaximumSubarraySumOfSizek(arr,k):
    i,j = 0,k-1
    ps = 0
    ans = float("-inf")
    while j < len(arr):
        if i==0:
            currSum = 0
            for l in range(i,j+1):
                currSum= currSum + arr[l]
            ps = currSum
        else:
            currSum = ps - arr[i-1]+arr[j]
            ps = currSum
        i+=1
        j+=1
        ans = max(ans,currSum)
    return ans



arr = [-3,4,-12,34,-67-54]
k = 3
print(getMaximumSubarraySumOfSizek(arr,k))