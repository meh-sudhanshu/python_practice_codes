def getMaximumSum(arr):
    ans = float("-inf")
    cts = 0
    for i in range(len(arr)):
        if cts < 0:
            cts = 0
        cts += arr[i]
        ans = max(cts,ans)
    return max(ans,cts)
def main():
    arr = [-2,3,-5,-6,9,2,-3,7,18,6,-5,100]
    ans = getMaximumSum(arr)
    print(ans)
main()