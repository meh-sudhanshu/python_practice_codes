def findNuberOfWaysToClimbStairs(n,dp):
    if dp[n] != 0:
        return dp[n]
    if n<=3:
        return n
    ans1 = findNuberOfWaysToClimbStairs(n-1,dp)
    dp[n-1] = ans1
    ans2 = findNuberOfWaysToClimbStairs(n-2,dp)
    dp[n-2] = ans2
    return ans1+ans2

def main():
    n = 50
    dp = [0 for i in range(n+1)]
    ans = findNuberOfWaysToClimbStairs(n,dp)
    print(ans)
main()