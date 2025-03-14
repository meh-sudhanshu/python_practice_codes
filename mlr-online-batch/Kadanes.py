
def getMaximumSubarraySum(arr):
    ans = float("-inf")
    sum = 0
    for i in range(len(arr)):
        ele = arr[i]
        sum += ele
        if sum > ans:
            ans = sum
        if sum < 0:
            sum = 0
    return ans



def main():
    arr = [-3,8,2,1,-3,-9,-19,2,3,8,3,-9,2,1]
    ans = getMaximumSubarraySum(arr)
    print(ans)

main()