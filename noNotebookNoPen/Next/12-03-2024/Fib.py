

def getSumTillN(n):
    if n<=0:return "Invalid input"
    if n==1: return 0
    if n==2: return 1
    a,b = 0,1
    _sum = a+b
    for i in range(3,n+1):
        _next = a+b
        _sum+=_next
        a = b
        b = _next
    return _sum

print(getSumTillN(10))