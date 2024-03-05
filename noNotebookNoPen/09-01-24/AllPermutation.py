
# arr = [1,2,3]
# [1] [[1]]

#  [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
def permute(arr):
    if len(arr) == 1:
        
    ans = []
    for i in range(len(arr)):
        fixedEle = arr[i]
        subArr = arr[0:i]+arr[i+1:]
        allPermutation = permute(subArr) #[[2,3],[3,2]]
        for p in allPermutation:
            currAns = [fixedEle]+p
            ans.append(currAns)
    return ans

arr = [1,2,3]
ans = permute(arr)
print(ans)