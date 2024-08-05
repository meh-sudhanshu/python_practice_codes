


def buildMatrix(_str):
    n = len(_str)
    dp = [[0 for i in range(n)] for j in range(n)]
    columnIndex = 0
    count = 0
    largest = ""
    smallest = ""
    smallestLength = float("+inf")
    while columnIndex < n:
        row = 0
        column = columnIndex 
        while column < n:
            if row == column:
                dp[row][column] = 1
                count+=1
                if(abs(column-row) > len(largest)):
                    largest = _str[row:column+1]
            elif abs(row-column) <= 2:
                if _str[row] == _str[column]:
                    dp[row][column] = 1
                    count+=1
                    if(abs(column-row) > len(largest)):
                        largest = _str[row:column+1]
                    if(abs(column-row) < smallestLength):
                        smallestLength = abs(column-row)
                        smallest = _str[row:column+1]
            else:
                if _str[row] == _str[column] and dp[row+1][column-1] == 1:
                    dp[row][column] = 1
                    count+=1
                    if(abs(column-row) > len(largest)):
                        largest = _str[row:column+1]
                    if(abs(column-row) < smallestLength):
                        smallestLength = abs(column-row)
                        smallest = _str[row:column+1]
            row+=1
            column+=1
        columnIndex+=1

    print("total number of palindromic substring ",count)
    print("largest palindromic substring ",largest)
    print("smallest palindromic substring",smallest)
    return dp







def main():
    _str = "malayala"
    n = len(_str)
    

    dp = buildMatrix(_str)
    for row in dp:
        for val in row:
            print(val,end=" ")
        print()
main()


