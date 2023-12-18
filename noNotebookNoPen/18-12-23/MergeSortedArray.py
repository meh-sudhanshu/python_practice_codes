

def mergeTwoSortedArray(arr1,arr2):
    n1,n2 = len(arr1), len(arr2)
    n = n1+n2
    ans = [0 for i in range(n)]
    i,j,k = 0,0,0
    while i<n1 and j<n2:
        if arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            i+=1
        else:
            ans[k] = arr2[j]
            j+=1
        k+=1

    if i<n1:
        while i<n1:
            ans[k] = arr1[i]
            i+=1
            k+=1
    if j<n2:
        while j<n2:
            ans[k] = arr2[j]
            j+=1
            k+=1
    return ans

arr1 = [-3,4,5,67,78,98]
arr2 = [-25,-13,0,1,4,7,9]
print(mergeTwoSortedArray(arr1,arr2))
    