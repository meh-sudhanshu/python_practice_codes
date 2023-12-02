
def brute_force(n,arr):
    for i in range(1,n+1):
        if i not in arr:
            return i


def xor_approach(n,arr):
    ans = 0
    for i in range(1,n+1):
        ans = ans^i
        if i!=n:
            ans = ans^arr[i-1]
    return ans

print(xor_approach(10,[3,4,1,2,6,5,8,10,9]))
