
arr = list(map(int,input().split()))
i, j = 0, len(arr)-1
while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i+=1
    j-=1
print(arr)