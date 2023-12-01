

def main():
    arr = [-2,3,4,-23,4,54,-67,78]
    queries = [[0,3],[1,3],[2,6],[4,7],[3,6]]
    ps = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:ps[i] = arr[i]
        else:  ps[i] = ps[i-1]+arr[i]
    for q in queries:
        si = q[0]
        ei = q[1]
        if si == 0:
            print(ps[ei])
        else:
            print(ps[ei]-ps[si-1])