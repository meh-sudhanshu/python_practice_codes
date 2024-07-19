

def diagonalParsing(arr):
    si,ei = 0,0
    n = len(arr)
    while ei < n:
        ce = ei
        while ce < n:
            print(arr[si][ce],end=" ")
            si+=1
            ce+=1
        si = 0
        ei+=1

def main():
    arr = [[3,9,-1,3,2],[0,2,8,-1,5],[0,0,6,6,7],[0,0,0,5,8],[0,0,0,0,3]]
    diagonalParsing(arr)
main()