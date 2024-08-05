


def printDiagonally(arr):
    n = len(arr)
    
    columnIndex = 0

    while columnIndex < n:
        row = 0
        column = columnIndex 
        while column < n:
            print(arr[row][column],end = " ")
            row+=1
            column+=1
        columnIndex+=1







def main():
    arr = [[3,2,9,8,9],[0,-1,6,7,3],[0,0,2,9,9],[0,0,0,5,2],[0,0,0,0,-1]]

    printDiagonally(arr)


main()


