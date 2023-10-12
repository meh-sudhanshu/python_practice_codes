def solve_n_queen(n,board,row,col,diag,rev_diag,asf):
    if row == n:
        print(asf)
        return
    for i in range(n):
        if col[i] == 0 and diag[row+i] == 0 and rev_diag[row-i+n-1]==0:
            board[row][i] = 1
            col[i] = 1
            diag[row+i] = 1
            rev_diag[row-i+n-1]=1
            solve_n_queen(n,board,row+1,col,diag,rev_diag,asf+str(row)+"->"+str(i)+" ")
            col[i] = 0
            diag[row+i] = 0
            rev_diag[row-i+n-1]=0








def main():
    n = 4
    board = [[0 for i in range(n)] for j in range(n)]
    col = [0 for i in range(n)]
    diag = [0 for i in range(2*n-1)]
    rev_diag = [0 for i in range(2*n-1)]
    solve_n_queen(n,board,0,col,diag,rev_diag,"")


main()