def trace(arr):
    n = len(arr)
    i,j = 0,0
    while j < n:
        i = 0
        jFlag = j
        while jFlag<n:
            print(arr[i][jFlag],end=" ")
            i+=1
            jFlag+=1
        print()
        j+=1
trace([[8,3,9,2],[0,6,5,9],[0,0,-3,2],[0,0,0,1]])
