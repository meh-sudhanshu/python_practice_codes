count = 0
def buildMatrix(_str):
    global count
    n = len(_str)
    dp = [[0 for i in range(n)]for j in range(n)]
    i,j = 0,0
    while j < n:
        i = 0
        jFlag = j
        while jFlag<n:
            if i==jFlag:
                dp[i][jFlag] = 1
                count+=1
            elif abs(i-j) <=2:
                if _str[i] == _str[jFlag]:
                    dp[i][jFlag] = 1
                    count+=1
            else:
                if _str[i] == _str[jFlag] and dp[i+1][jFlag-1] == 1:
                    dp[i][jFlag] = 1
                    count+=1
            i+=1
            jFlag+=1
        print()
        j+=1
    return dp

def printMatrix(dp):
    for row in dp:
        for val in row:
            print(val,end=" ")
        print()


dp = buildMatrix("axaxa")
print(count,"number of plaindromic substring")
printMatrix(dp)
