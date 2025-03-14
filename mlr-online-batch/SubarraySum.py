


def getMaximumSubarraySumOfSizeK(arr,k):
    i = 0
    j = k-1
    ans = float("-inf")
    sum = 0
    while j < len(arr):
        if i == 0:
            for l in range(i,j+1):
                sum = sum + arr[l]
        else:
            sum = sum - arr[i-1] + arr[j]
        i+=1
        j+=1
        if sum > ans:
            ans = sum
    return ans
        





def main():
    arr = [-11,2,6,-2,6,8,-4,32,-56,-32]
    k = 3
    ans = getMaximumSubarraySumOfSizeK(arr,k)
    print(ans)

main()
