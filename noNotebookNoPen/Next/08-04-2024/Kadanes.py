def main():
    arr = [-3,1,2,-1,-5,2,6,9,-1]
    ans = float("-inf")
    cts = 0
    for i in range(len(arr)):
        cts = cts+arr[i]
        if cts > ans:
            ans = cts
        if cts < 0:
            cts = 0
    print(max(ans,cts))
main()