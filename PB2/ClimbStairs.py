def getAns(n):
    if n<=3:
        return n
    return getAns(n-1)+getAns(n-2)
print(getAns(6))