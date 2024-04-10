def isPairExist(a,t):
    a.sort()
    i,j = 0, len(a)-1
    while i<j:
        if a[i]+a[j] == target: return True
        if a[i]+a[j] > target: j-=1
        if a[i]+a[j] < target: i+=1
    return False


def main():
    arr = [6,6,1,-3,9,-3,-23,4,-56,9,13,24,35]
    target = 6
    ans = isPairExist(arr,target)
    print(ans)
main()