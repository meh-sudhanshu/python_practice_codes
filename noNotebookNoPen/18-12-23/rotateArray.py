def rotateArray(arr,i):
    stack = []
    queue = []
    for j in range(i):
        queue.append(arr[j])
    for j in range(i,len(arr)):
        stack.append(arr[j])
    j = 0
    while len(stack) > 0:
        arr[j] = stack.pop()
        j+=1
    while len(queue) > 0:
        arr[j] = queue.pop(0)
        j+=1
    return arr


arr = [3,2,4,5,6,7,8,9]
i = 5
print(rotateArray(arr,i))