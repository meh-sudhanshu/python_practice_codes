def multiSolver(str):
    n = len(str)
    dp = [[0 for i in range(n)] for j in range(n)]
    j = 0
    ans = 0
    while j < n:
        i = 0
        jflag = j
        
        while jflag <n:
            if i == jflag:
                dp[i][jflag] = 1
                ans+=1
            elif jflag == 1 or jflag == 2:
                if str[i] == str[jflag]:
                    dp[i][jflag] = 1
                    ans+=1
                else:
                    dp[i][jflag] = 0
            else:
                if str[i] == str[jflag]:
                    dp[i][jflag] = dp[i+1][jflag-1]
                    if dp[i][jflag] == 1:
                        ans+=1
                else:
                    dp[i][jflag] = 0
            i+=1
            jflag+=1
        j+=1

    return ans

print(multiSolver("madam"))
        
