def main():
    arr = [[1,5,8,10],[0,2,6,9],[0,0,3,7],[0,0,0,4]]
    n = 4
    globalJ = 0
    while globalJ<n:
        i = 0
        j = globalJ
        while j < n:
            print(arr[i][j],end=" ")
            i+=1
            j+=1
        print()
        globalJ+=1

main()

