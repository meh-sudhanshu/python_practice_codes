def getCount(n):
    if dp[n] != -1:
        return dp[n]
    if n == 1 or n==2:
        dp[n] = n
        return n
    ans1 = getCount(n-1)
    ans2 = getCount(n-2)
    dp[n-1] = ans1
    dp[n-2] = ans2
    return ans1+ans2

n = 10
dp = [-1 for i in range(n+1)]
ans = getCount(n,dp)