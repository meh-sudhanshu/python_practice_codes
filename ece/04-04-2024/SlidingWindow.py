def getMaximumWindowSum(arr,ws):
    i,j = 0, ws-1
    ans = float("-inf")
    ps = 0
    si, ei = -1, -1
    while j<len(arr):
        if i==0:
            cs = sum(arr[i:j+1])
            si = i
            ei = j
            ps = cs
        else:
            cs = ps-arr[i-1]+arr[j]
            ps = cs
        if cs > ans :
            ans = cs
            si = i
            ei = j
        i+=1
        j+=1
    return ans,i,j
def main():
    arr = [2,-9,8,-1,-3,5,16,-3]
    ws = 3
    print(getMaximumWindowSum(arr,ws))
main()