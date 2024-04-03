def main():
    n = 6
    arr = [2,1,5,4,6]
    ans = 0
    for i in range(1,n+1): ans=ans^i
    for i in range(5): ans=ans^arr[i]
    print(ans)
main()
