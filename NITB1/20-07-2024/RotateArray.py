def rotateArr(arr,pi):
    st = []
    queue = []
    for i in range(len(arr)):
        if i < pi:
            queue.append(arr[i])
        else:
            st.append(arr[i])
    i = 0
    while len(st) > 0:
        arr[i] = st.pop()
        i+=1
    while len(queue) > 0:
        arr[i] = queue.pop(0)
        i+=1
    return arr




def main():
    arr = [2,3,4,8,9,12,5]
    pi = 3
    arr = rotateArr(arr,3)
    print(arr)
main()