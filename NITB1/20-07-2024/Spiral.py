

def printSpiral(arr):
    turn = 1
    count = 0
    n = len(arr)
    totalPrint = len(arr)*len(arr[0])
    fdri,fdcsi,fdcei = 0,0,n-1
    sdci,sdrsi,sdrei = n-1,1,n-1
    while count < totalPrint:
        if turn == 1:
            for i in range(fdcsi,fdcei+1):
                print(arr[fdri][i,end=" "])
            fdri+=1
            fdcsi+=1
            fdcei-=1
            turn = 2
        elif turn == 2:
            for i in range(sdrsi,sdrei+1):
                print(arr[i][sdci],end=" ")
            sdci-=1
            sdrsi+=1
            sdrei-=1
            turn = 3
        elif turn == 3:
            pass
            turn = 4
        else:
            pass
            turn = 1





def main():
    arr = [[8,-3,9,2],[9,3,2,8],[1,10,11,15],[8,9,15,14]]
    printSpiral(arr)

main()