


def mergeSortedArray(arr1,arr2):
    n1 =len(arr1)
    n2 =len(arr2)
    ans = [0 for i in range(n1+n2)]
    i,j,k = 0,0,0
    while i<n1 or j<n2:
        if i>=n1:
            while j<n2:
                ans[k] = arr2[j]
                k+=1
                j+=1
        elif j>=n2:
            while i<n1:
                ans[k] = arr1[i]
                i+=1
                k+=1
        else:
            if arr1[i] < arr2[j]:
                ans[k] = arr1[i]
                i+=1
                k+=1
            else:
                ans[k] = arr2[j]
                j+=1
                k+=1
    print(ans)

arr1 = [1,3,6,8,9,90]
arr2 = [-3,4,7,8,9,10]


mergeSortedArray(arr1,arr2)



