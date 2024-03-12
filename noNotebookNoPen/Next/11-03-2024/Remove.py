

arr = list(map(int,input().split()))
num = int(input())
for i in range(len(arr)):
    if arr[i] == num:
        arr.remove(arr[i])
print(arr)