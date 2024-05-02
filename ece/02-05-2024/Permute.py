def permute(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [arr]
    ans = []
    for i in range(n):
        fe = arr[i]
        subArr = arr[0:i]+arr[i+1:]
        allPer = permute(subArr)
        for per in allPer:
            ans.append([fe]+per)
    return ans

ans = permute([1,2,3])
print(ans)