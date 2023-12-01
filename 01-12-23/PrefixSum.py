def main():
    arr = [-3,4,5,2,3,-89,45,98]
    queries = [[0,2],[1,3],[2,5]]
    ans=[]
    ps=[0 for i in range(len(arr))] 
    for i in range(len(arr)):
        if i ==0 :
            ps[i] = arr[i]
        else:
            ps[i]=ps[i-1]+arr[i]
    for query in queries:
        si = query[0]
        ei = query[1]
        currAns = ps[ei]-ps[si-1]
        ans.append(currAns)
    print(ans)
main() 