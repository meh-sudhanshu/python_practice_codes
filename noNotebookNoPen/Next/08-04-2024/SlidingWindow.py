def main():
    arr = [-2,4,1,2,-5,-3,-5,60,4,-1,4,2,-5]
    ws = 4
    i,j = 0, ws-1
    ans = float("-inf")
    ps = 0
    while j < len(arr):
        if i == 0:
            cs = sum(arr[i:j+1])
            ps = cs
        else:
            cs = ps-arr[i-1]+arr[j]
            ps = cs
        i+=1
        j+=1
        ans = max(ans,cs)
    print(ans)

main()

