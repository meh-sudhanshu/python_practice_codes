def main():
    _str = "madammadam"
    #a = int(input())
    n = len(_str)
    dp = [[0 for i in range(n)] for j in range(n)]
    #print(dp)
    i,j = 0,0
    count = 0
    while j < n:
        jflag = j
        while jflag < n:
            if i == jflag:
                dp[i][jflag] = 1
                count+=1
                
            elif abs(i-jflag) == 1:
                if _str[i]==_str[jflag]:
                    dp[i][jflag]=1
                    count+=1
                else:
                    dp[i][jflag]=0
            else:
                if _str[i]==_str[jflag]:
                    if dp[i+1][jflag-1]==1:
                        dp[i][jflag]=1
                        count+=1
                    else:
                        dp[i][jflag]=0
                else:
                    dp[i][jflag]=0
            i+=1
            jflag+=1
        j+=1
        i=0
    #print(dp)
    return count

print(main())

