

def getMaximumSubarraySum(arr):
    ans = float('-inf')
    i = 0
    flag = True
    cs = 0
    for i in range(len(arr)):
        if cs < 0:
            cs = 0
        if arr[i] >=0 :
            cs+= arr[i]
            ans = max(ans,cs)
            flag = False
        else:
            ans = max(ans,cs)
            cs+=arr[i]
    if flag == True:
        return max(arr)
    return max(ans,cs)


arr = [-3,-2,-1,-5,-7,-8,-9,-11,-13,-6,-12]
print(getMaximumSubarraySum(arr))


