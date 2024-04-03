def isPairExist(a,t):
    a.sort()
    i,j = 0, len(a)-1
    while i<j:
        if a[i]+a[j] == t: return True
        if a[i]+a[j] < t: i+=1
        if a[i]+a[j] > t: j-=1
    return False

def main():
    arr = [-2,4,1,5,7,-89,56,87]
    target = 600
    print(isPairExist(arr,target))
main()