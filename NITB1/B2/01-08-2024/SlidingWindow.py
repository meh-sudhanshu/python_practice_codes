


def getMaximumSum(arr,k):
    i = 0
    j = k-1
    ans = float("-inf")
    ps = 0
    while j < len(arr):
        _sum = 0
        if i == 0:
            _sum = sum(arr[i:j+1])
            ps = _sum
        else:
            _sum = ps - arr[i-1]+arr[j]
            ps = _sum
        i+=1
        j+=1
        ans = max(ans,_sum)

    return ans







def main():
    arr = [2,3,-5,6,7,8]
    k = 3
    ans = getMaximumSum(arr,k)
    print(ans)

main()