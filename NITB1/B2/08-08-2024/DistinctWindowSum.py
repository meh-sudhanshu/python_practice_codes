


def getMaximumSubArraySumWithDistinctElement(arr,k):
    ans = float("-inf")
    cs , ps = 0, 0
    i,j = 0, k-1
    myDict = {}
    while j < len(arr):
        if i == 0:
            for k in range(i,j+1):
                if arr[k] not in myDict:
                    myDict[arr[k]] = 1
                else:
                    oldValue = myDict[arr[k]]
                    oldValue+=1
                    myDict[arr[k]] = oldValue
                    # myDict[key]+=1
                cs+=arr[k]
            if  len(myDict) == k and cs > ans:
                print("triggered")
                print(ans)
                ans = cs
            ps = cs
        else:
            removedValueFrequency = myDict[arr[i-1]]
            if removedValueFrequency == 1:
                del myDict[arr[i-1]]
            else:
                myDict[arr[i-1]]-=1
            if arr[j] in myDict:
                myDict[arr[j]]+=1
            else:
                myDict[arr[j]] = 1
            cs = (ps- arr[i-1])+arr[j]
            if  len(myDict) == k and  cs > ans:
                print("triggere")
                ans = cs
                print(ans)
            ps = cs
        i+=1
        j+=1
        #print(ans)
        #print(myDict)
    return ans




def main():
    arr = [-3,-3,2,9,12,8,16,7,16,-3,2]
    k = 5
    ans = getMaximumSubArraySumWithDistinctElement(arr,k)
    print(ans)


main()