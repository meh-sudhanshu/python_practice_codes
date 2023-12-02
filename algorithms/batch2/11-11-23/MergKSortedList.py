
# arr = [[1,2,3,4]]

def mergeTwoSortedList(arr1,arr2):
    ans = [0 for i in range(len(arr1)+len(arr2))]
    i,j,k = 0,0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            i+=1
            k+=1
        else:
            ans[k] = arr2[j]
            j+=1
            k+=1
    if i < len(arr1):
        while i < len(arr1):
            ans[k] = arr1[i]
            i+=1
            k+=1

    if j < len(arr2):
        while j < len(arr2):
            ans[k] = arr2[j]
            j+=1
            k+=1
    return ans
    




def mergeKSortedList(arr):
    if len(arr) == 1:
        return arr[0]
    i = 0
    ans = []
    while i < len(arr):
        if i == 0:
            ans = mergeTwoSortedList(arr[0],arr[1])
            i = 2
        else:
            ans = mergeTwoSortedList(ans,arr[i])
            i+=1
    print(ans)


arr = [[1,3,5,7],[2,4,7,9,11],[101,202,303],[45],[116]]
mergeKSortedList(arr)
    
