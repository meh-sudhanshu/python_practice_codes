

def printSpiral(arr,n):
    fdri, fdcsi, fdcei = 0, 0, n-1
    sdci, sdrsi, sdrei = n-1, 1, n-1
    tdri, tdcsi, tdcei = n-1, n-2, 0
    fdci, fdrsi, fdrei = 0, n-2, 1
    turn = 1

    total = n*n
    count = 0

    while count <= total:
        if turn == 1:
            for col in range(fdcsi,fdcei+1):
                print(arr[fdri][col],end=" ")
                count+=1
            fdri+=1
            fdcsi+=1
            fdcei-=1
            turn = 2
        elif turn == 2:
            for row in range(sdrsi,sdrei+1):
                print(arr[row][sdci],end=" ")
                count+=1
            sdci-=1
            sdrei-=1
            sdrsi+=1
            turn = 3
        elif turn == 3:
            for col in range(tdcsi,tdcei-1,-1):
                print(arr[tdri][col],end=" ")
                count+=1
            tdri-=1
            tdcei+=1
            tdcsi-=1
            turn = 4
        else:
            for row in range(fdrsi,fdrei-1,-1):
                print(arr[row][fdci],end=" ")
                count+=1
            fdci+=1
            fdrei+=1
            fdrsi-=1
            turn  = 1









def main():
    arr = [[3,2,1,4],[9,3,4,5],[-3,2,6,7],[10,9,8,-1]]
    n = len(arr)
    printSpiral(arr,n)

main()