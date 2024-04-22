def main():
    arr = [3,-1,2,0,5,9,6,7]
    queries = [[0,2],[1,4],[3,5],[4,7]]
    ps = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = arr[i]+ps[i-1]
    for q in queries:
        si,ei = q[0],q[1]
        if si == 0: print(ps[ei])
        else: print(ps[ei]-ps[si-1])
main()