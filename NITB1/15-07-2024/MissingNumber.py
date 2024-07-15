
def getMissingNumber(n,arr):
    ans = 0
    for i in range(1,n+1):
        ans = ans^i
    for e in arr : ans = ans^e

    return ans


def main():
    n = 10
    arr = [3,2,4,8,9,10,1,5,8,7]

    ans = getMissingNumber(n,arr)
    print(ans)