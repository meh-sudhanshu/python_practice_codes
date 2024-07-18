


def getMaximumSubarraySum(arr,k):
    i = 0
    j = k-1
    ans = float("-inf")
    ps = 0
    while j < len(arr):
        cs = 0
        if i == 0:
            cs = sum(arr[i:j+1])
            ps = cs
        else:
            cs = ps-arr[i-1]+arr[j]
            ps = cs
        i+=1
        j+=1
        ans = max(cs,ans)



def main():
    arr = [-3,2,5,-1,3,9,-1,-2,3,4]
    k = 3
    ans = getMaximumSubarraySum(arr,k)
    print(ans)
main()