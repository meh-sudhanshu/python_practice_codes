from time import *

def fun(n):
    if n<=2: return n
    return fun(n-2)+fun(n-4)
# start_time = perf_counter()
# ans = fun(16)
# sleep(0)
# end_time = perf_counter()
# print((end_time-start_time)*1000," ms")

dp =  [-100 for i in range(17)]
def optimised_fun(n):
    global dp 
    if dp[n] != -100:
        return dp[n]
    if n<=2:
        dp[n] = n
        return n
    ans1 = fun(n-2)
    ans2 = fun(n-4)
    dp[n-2] = ans1
    dp[n-4] = ans2
    return ans1+ans2
print(optimised_fun(16))
    