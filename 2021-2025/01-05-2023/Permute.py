def permute(arr):
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        fe = arr[i]
        subArr = arr[0:i]+arr[i+1:]
        _all = permute(subArr)
        for v in _all:
            ans.append([fe]+v)
    return ans

ans = permute([3,2,8])
print(ans)