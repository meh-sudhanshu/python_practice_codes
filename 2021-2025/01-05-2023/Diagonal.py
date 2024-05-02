def traceDiagonally(arr):
    n = len(arr)
    i,j = 0,0
    while j< n:
        i = 0
        jFlag = j
        while jFlag < n:
            print(arr[i][jFlag],end= " ")
            i+=1
            jFlag+=1
        print()
        j+=1

traceDiagonally([[3,9,2,1],[0,6,8,-3],[0,0,5,2],[0,0,0,0]])
