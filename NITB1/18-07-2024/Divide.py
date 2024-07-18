

def getResult(dividend,divisor):
    if dividend == divisor:
        return 1
    sign = 1
    if dividend > 0 and divisor < 0:
        sign = -1
    if divisor > 0 and dividend < 0:
        sign = -1
    n = abs(dividend)
    d = abs(divisor)
    quotient = 0
    while n >= d:
        count = 0
        while n >= d<<(count+1):
            count+=1
        n = n - (d<<count)
        quotient += 1<<count
    return quotient
        
        
def main():
    dividend = 35
    divisor = 4 
    ans = getResult(dividend,divisor)
    print(ans)
main()