def main():
    arr = [-1,3,-2,5,6,-1,8,-3]
    queries = [[0,4],[1,6],[3,7],[0,4],[1,4]]
    ps = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i-1]+arr[i]
    for q in queries:
        si,ei = q[0],q[1]
        if si == 0: print(ps[ei])
        else:
            print(ps[ei]-ps[si-1])
main()
