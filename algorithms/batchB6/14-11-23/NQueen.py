

def NQueen(n,board,row,col,diag,revDiag,csf):
    if row == n-1:
        print(csf)
        return
    for i in range(n):
        if col[i] == 0 and diag[row-i] == 0 and revDiag[row-i+n-1]==0:
            col[i]=1
            diag[row-i]=1
            revDiag[row-i+n+1]=1
            NQueen(n,board,row+1,col,diag,revDiag,csf+str(row)+"->"+str(i))
            col[i]=0
            diag[row-i]=0
            revDiag[row-i+n+1]=0

n = 4
board = [[0 for i in range(n)] for j in range(n)]
col = [0 for i in range(n)]
diag = [0 for i in range(2*n+1)]
revDiag = [0 for i in range(2*n+1)]

NQueen(n,board,0,col,diag,revDiag,"")
