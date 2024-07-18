


def getMaximumSubarraySumWithDistinceElement(arr,k):
    i = 0
    j = k-1
    ans = float("-inf")
    ps = 0
    _map = {}
    while j < len(arr):
        cs = 0
        if i == 0:
            cs = 0
            for k1 in range(i,j+1):
                cs+=arr[k1]
                if arr[k1] in _map:
                    value = _map[arr[k1]]
                    value+=1
                    _map[arr[k1]] = value
                else:
                    _map[arr[k1]] = 1
            ps = cs
        else:
            key = arr[i-1]
            if _map[key] == 1:
                del _map[arr[i-1]]
            else:
                _map[key] = _map[key]-1
            if arr[j] in _map:
                _map[arr[j]]+=1
            else:
                _map[arr[j]] = 1
            cs = ps-arr[i-1]+arr[j]
            ps = cs
        i+=1
        j+=1
        if len(_map) == k and cs>ans:
            ans = cs
    
    return ans



def main():
    arr = [2,2,-3,9,9,-3,9,-2,4,6,-5,9]
    k = 3
    ans = getMaximumSubarraySumWithDistinceElement(arr,k)
    print(ans)
main()