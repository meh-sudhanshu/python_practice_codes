def traceDiagonally(_str):
    n = len(_str)
    dp = [[0 for i in range(n)] for j in range(n)]
    i,j = 0,0
    while j< n:
        i = 0
        jFlag = j
        while jFlag < n:
            if i == jFlag:
                dp[i][jFlag] = 1
            elif abs(i-jFlag) <= 2:
                if _str[i] == _str[jFlag]:
                    dp[i][jFlag] = 1
            else:
                if _str[i] == _str[jFlag] and dp[i+1][jFlag-1] ==1:
                    dp[i][jFlag] = 1
            i+=1
            jFlag+=1
        j+=1
    return dp
_str = "malyalam"
dp = traceDiagonally(_str)
for row in dp:
    for v in row:
        print(v,end=" ")
    print()