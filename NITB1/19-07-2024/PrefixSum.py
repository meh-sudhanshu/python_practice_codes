




def main():
    arr = [-3,2,9,8,-3,5,2,1]
    n = len(arr)
    queries = [[5,7],[2,7],[1,6],[3,7],[0,4]]
    prefixSum = [0 for i in range(n)]

    for i in range(n):
        if i == 0: prefixSum[i] = arr[i]
        else: prefixSum[i]  = prefixSum[i-1]+arr[i]
    
    for query in queries:
        si = query[0]
        ei = query[1]

        if si == 0:
            print(prefixSum[ei],end= " ")
        else:
            print(prefixSum[ei]-prefixSum[si-1],end=" ")

main()
    