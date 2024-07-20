

def printSpiral(arr):
    turn = 1
    count = 0
    n = len(arr)
    totalPrint = len(arr)*len(arr[0])
    fdri,fdcsi,fdcei = 0,0,n-1
    sdci,sdrsi,sdrei = n-1,1,n-1
    tdri, tdcsi, tdcei = n-1, n-2, 0
    fdci, fdrsi,fdrei = 0, n-2, 1
    while count < totalPrint:
        if turn == 1:
            #print("first")
            for i in range(fdcsi,fdcei+1):
                print(arr[fdri][i],end=" ")
                count+=1
            fdri+=1
            fdcsi+=1
            fdcei-=1
            turn = 2
        elif turn == 2:
            #print("second")
            for i in range(sdrsi,sdrei+1):
                print(arr[i][sdci],end=" ")
                count+=1
            sdci-=1
            sdrsi+=1
            sdrei-=1
            turn = 3
        elif turn == 3:
            #print("third")
            for i in range(tdcsi,tdcei-1,-1):
                print(arr[tdri][i],end=" ")
                count+=1
            tdri-=1
            tdcsi-=1
            tdcei+=1
            turn = 4
        else:
            #print("fourth")
            for i in range(fdrsi,fdrei-1,-1):
                print(arr[i][fdci],end=" ")
                count+=1
            fdci+=1
            fdrsi-=1
            fdrei+=1
            turn = 1

def main():
    arr = [[8,-3,9,2],[9,3,2,8],[1,10,11,15],[8,9,15,14]]
    printSpiral(arr)

main()