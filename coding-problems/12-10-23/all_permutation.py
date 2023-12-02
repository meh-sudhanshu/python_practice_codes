def permute(arr):
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        temp_ans = [arr[i]]
        sub_arr = arr[0:i]+arr[i+1 :]
        p_arr = permute(sub_arr)
        for e in p_arr:
            ans.append(temp_ans+e)
    return ans

print(permute([1,2,3]))