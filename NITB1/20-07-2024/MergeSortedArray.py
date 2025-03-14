

def mergeArrays(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [0 for i in range(len(arr1)+len(arr2))]
    i,j,k = 0,0,0

    while i< len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i+=1
            k+=1
        else:
            arr3[k] = arr2[j]
            j+=1
            k+=1

    while i < len(arr1):
        arr3[k] = arr1[i]
        i+=1
        k+=1
    while j < len(arr2):
        arr3[k] = arr2[j]
        j+=1
        k+=1

    return arr3








def main():
    arr1 = [8,9,12,15,18]
    arr2 = [-3,5,6,8,180,181,183,185]

    ans = mergeArrays(arr1,arr2)
    print(ans)

main()