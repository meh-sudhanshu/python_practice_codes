


def nQueen(n,row,col,dia,revDiag,psf):
    #base condition
    if row == n:
        print(psf)
        return

    for i in range(n):
        if col[i] == 0 and revDiag[i+row] == 0 and dia[i-row+n-1] == 0:
            col[i]=1
            revDiag[i+row]=1
            dia[i-row+n-1]=1
            nQueen(n,row+1,col,dia,revDiag, psf+str(row)+"->"+str(i)+",")
            col[i]=0
            revDiag[i+row]=0
            dia[i-row+n-1]=0








def main():
    n = 4
    col = [0 for i in range(n)]
    dia = [0 for i in range((2*n)-1)]
    revDiag = [0 for i in range((2*n)-1)]
    nQueen(n,0,col,dia,revDiag,"")


main()
   