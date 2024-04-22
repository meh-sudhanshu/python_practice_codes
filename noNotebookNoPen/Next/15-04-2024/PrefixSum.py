def main():
    arr = [-1,2,4,2,-3,-3,-2,3,-2,1,65,76,34]
    queries=[[0,2],[1,5],[0,3],[3,6]]
    ps = [0 for i in range(len(arr))]
    for i in range(len(ps)):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i-1]+arr[i]
    for query in queries:
        si,ei = query[0],query[1]
        if si == 0: print(ps[ei],end=" ")
    e    else:  print(ps[ei] - ps[si-1],end=" ")

main()