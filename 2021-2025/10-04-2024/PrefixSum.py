def getAllQueryAns(arr,query):
    ps = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i-1]+arr[i]
    for q in query:
        si,ei = q[0],q[1]
        if si == 0: print(ps[ei])
        else: print(ps[ei]-ps[si-1])

def main():
    arr = [2,3,1,-5,-3,2,4,-5]
    query = [[0,4],[2,5],[1,6]]
    ans = getAllQueryAns(arr,query)
    print(ans)
main()