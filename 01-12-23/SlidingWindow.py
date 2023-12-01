def main():
    arr =[-2,3,2,3,45,67,-98,-4, ]
    k = 3
    ans = float('-inf')
    ps = 0
    i,j = 0,k-1
    while j < len(arr):
        if i == 0:
            currSum = sum(arr[i:j+1])
            ps = currSum
        else:
            currSum = ps-arr[i-1]+arr[j]
        i+=1
        j+=1
        ans = max(ans,currSum)
    print(ans)

main()
