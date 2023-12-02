def permute(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        fixedElement = arr[i]
        subarray = arr[0:i]+arr[i+1:]
        allPermutation = permute(subarray)
        for permutation in allPermutation:
            ans.append([fixedElement]+permutation)
    return ans    

arr = [1,2,3,4]
print(permute(arr))