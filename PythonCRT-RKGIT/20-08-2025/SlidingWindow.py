
def getMaximumSubarraySumOfSizeK(arr,k):
    i,j = 0, k-1
    ans = float("-inf")
    sum = 0
    while j < len(arr):
        if i == 0:
            for l in range(i,j+1): sum+=arr[l]
        else:
           sum =  sum - arr[i-1] + arr[j]
        i+=1
        j+=1
        if sum > ans: ans = sum
    return ans



def main():
    # arr = list(map(int,input().split(" ")))
    arr = [-3,0,4,2,6,-9,3,-5,4]
    k = 3
    ans = getMaximumSubarraySumOfSizeK(arr,k)
    print(ans)
    
main()
    