
def mergeTwoSortedList(arr1,arr2):
    ans = []
    return ans





def mergeKSortedList(arr):
    ans = []
    if len(arr) == 1:
        return arr[0]
    else:
        ans = mergeTwoSortedList(arr[0],arr[1])

    i = 2
    while i < len(arr):
        ans = mergeTwoSortedList(ans,arr[i])
        i+=1
        
    print(ans)


