def main():
    arr = [-1,2,4,-2,4,2,-6,7,-8,3]
    ws = 4
    ans = float("-inf")
    ps = 0
    i,j = 0, ws-1
    si, ei = 0, ws-1
    while j < len(arr):
        if i == 0:
            cs = sum(arr[i:j+1])
            ans = cs
            ps = cs
        else:
            cs = ps - arr[i-1]+arr[j]
            ps = cs
            if cs > ans:
                si = i
                ei = j
                ans = cs
        i+=1
        j+=1
    print(ans,si,ei)
main()
