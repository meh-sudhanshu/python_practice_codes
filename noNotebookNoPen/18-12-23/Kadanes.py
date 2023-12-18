

def getMaximumSubarraySum(arr):
    ans = float("-inf")
    cs = 0
    for i in range(len(arr)):
        if cs < 0:
            cs = 0
        else:
            if arr[i] >=0:
                cs += arr[i]
            if arr[i] < 0:
                ans = max(ans,cs)
                cs+=arr[i]
    if max(cs,ans) == 0:
        arr.sort()
        return arr[-1]
    return max(cs,ans)
        
arr = [-3,-9,-2,-11,-8,-7,-6,-5,-13]
print(getMaximumSubarraySum(arr))