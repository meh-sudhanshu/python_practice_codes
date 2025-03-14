




def fun(n,dp):
    if n<=2:
        dp[n] = -1
        return -1

    if dp[n] != 0:
        return dp[n]

    ans1 = fun(n-2,dp)
    dp[n-2] = ans1

    ans2 = fun(n-4,dp)
    dp[n-4] = ans2

    return n+ans1+ans2



def main():
    n = 10
    dp = [0 for i in range(n+1)]
    ans = fun(n,dp)
    print(ans)

main()