def mergeList(arr1, arr2):
    n = len(arr1)+len(arr2)
    ans = [0 for i in range(n)]
    i,j,k = 0,0,0     
    while i<len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            i+=1
        else:
            ans[k] = arr2[j]
            j+=1
        k+=1
    while i < len(arr1):
        ans[k] = arr1[i]
        i+=1
        k+=1
    
    while j< len(arr2):
        ans[k] = arr2[j]
        k+=1
        j+=1

    return ans


def main():
    arr1 = [-2,3,4,7,89]
    arr2 = [-34,0,1,5,9,89]
    ans = mergeList(arr1,arr2)
    print(ans)

main()