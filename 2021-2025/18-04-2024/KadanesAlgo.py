def main():
    arr = [-3,-2,5,-6,8,9,2,-1,-6]
    ans = float("-inf")
    cts = 0
    for i in range(len(arr)):
        cts+=arr[i]
        ans = max(ans,cts)
        if cts < 0:
            cts = 0
    print(ans)