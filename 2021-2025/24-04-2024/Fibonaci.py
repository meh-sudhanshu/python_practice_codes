import time
def getNthNumber(n):
    if n == 1: return 0
    if n == 2: return 1
    return getNthNumber(n-1)+getNthNumber(n-2)

n = 5
dp = [-1 for i in range(n+1)]
_sum = 0
startTime = time.time()
for i in range(1,n+1):
    if dp[i] != -1:
        _sum+=dp[i]
    else:
        nthNumber = getNthNumber(i)
        dp[i] = nthNumber
        _sum+=nthNumber
print(_sum)
endTime = time.time()
print("total time taken = ", endTime-startTime)
