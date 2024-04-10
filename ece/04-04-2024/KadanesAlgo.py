def kadanesAlgo(arr):
    ans = float("-inf")
    cts = 0
    for i in range(len(arr)):
        cts+=arr[i]
        if cts > ans: ans = cts
        if cts < 0: cts = 0
    return ans

def main():
    arr = [-3,-4,-1,-6,-4,-5,-7,-9,-3,-4,-6]
    print(kadanesAlgo(arr))
main()

