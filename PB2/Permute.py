def permute(arr):
    if len(arr) == 0:return []
    if len(arr) == 1:return [arr] 
    ans = []
    for i in range(len(arr)):
        fixedEle = arr[i]
        subArray = arr[0:i]+arr[i+1:]
        allPer = permute(subArray)
        for per in allPer:
            ans.append([fixedEle]+per)
    return ans


arr = [1,2,3]
print(permute(arr))