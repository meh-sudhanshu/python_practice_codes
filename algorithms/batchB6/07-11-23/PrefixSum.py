

def getQueriesSum(arr,queries):
    n = len(arr)
    ps = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i-1]+arr[i]
    for query in queries:
        si , ei = query[0], query[1]
        if si == 0:
            print(ps[ei])
        else:
            print(ps[ei]-ps[si-1])