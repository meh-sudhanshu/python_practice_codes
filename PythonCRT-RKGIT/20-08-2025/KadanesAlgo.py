

def main():
    arr = [-3,0,4,2,6,-9,3,-5,4]
    ans = float("-inf")
    sum = 0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum > ans: ans = sum
        if sum < 0:
            sum = 0
    print(ans)
main()