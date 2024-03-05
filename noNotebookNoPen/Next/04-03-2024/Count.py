


def count(n):
    ans = 0
    for i in range(1,n+1):
        i = str(i)
        c1 = i.count('1')
        c7 = i.count('7')
        ans+=(c1+c7)
    return ans

print(count(11))