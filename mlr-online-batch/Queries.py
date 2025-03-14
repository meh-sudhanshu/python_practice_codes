

def getQueiresAns(arr,queries):
    ans = []
    n = len(arr)
    prefixSum = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            prefixSum[i] = arr[i]
        else:
            prefixSum[i] = prefixSum[i-1]+arr[i]
    for query in queries:
        si = query[0]
        ei = query[1]
        if si == 0:
            ans.append(prefixSum[ei])
        else:
            ans.append(prefixSum[ei]-prefixSum[si-1])
    return ans
        

def main():
    arr = [3,8,0,-3,2,3,7]
    queries = [[1,4],[2,5],[0,6]]
    ans = getQueiresAns(arr,queries)
    print(ans)
main()