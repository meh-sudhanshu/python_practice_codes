def main():
    n = 8
    arr = [2,1,4,3,6,8,5]
    ans = 0
    for i in range(1,n+1): ans = ans^i
    for i in range(n-1): ans = ans^arr[i]
    print(ans)
main()