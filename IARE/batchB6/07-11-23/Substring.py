

def multiSolver(str):
    n = len(str)
    dp = [[0 for i in range(n)] for j in range(n)]
    j = 0
    while j <n:
        i = 0
        jflag = j
        while jflag <n:
            # do some work
            if j == 0:
                dp[i][jflag] = 1
            else:
                if str[i] != str[jflag]:
                    dp[i][jflag] = 0
                else:
                    
                    dp[i][jflag] = dp[i+1][jflag-1]
            jflag+=1
            i+=1
        j+=1
