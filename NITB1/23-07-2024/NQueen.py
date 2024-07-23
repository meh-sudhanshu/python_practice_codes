


def nQueen(n,board,row,diag,revDiag,col,csf):
    if row == n:
        print(csf)
        return
    for i in range(n):
        if col[i] == 0 and diag[n+row-i] == 0 and revDiag[row+i] == 0:
            col[i] = 1
            diag[n+row-i] = 1
            revDiag[row+i] = 1
            nQueen(n,board,row+1,diag,revDiag,col,csf+str(row)+str(i)+"->")
            col[i] = 0
            diag[n+row-i] = 0
            revDiag[row+i] = 0




def main():
    n = 4
    board = [[0 for i in range(n)] for j in range(n)]
    col = [0 for i in range(n)]
    revDiag = [0 for i in range(2*n-1)]
    diag = [0 for i in range(2*n-1)]
    nQueen(n,board,0,diag,revDiag,col,"")

main()