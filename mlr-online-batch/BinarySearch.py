


def binarySearch(arr,searchValue):
    i,j = 0, len(arr)-1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] == searchValue:
            return True
        if arr[mid] > searchValue:
            j = mid-1
        if arr[mid] < searchValue:
            i = mid+1
    return False



def main():
    # sorted array
    arr = [-12,-3,4,5,12,32,42,56,67,87,98]
    searchValue = 3200
    ans = binarySearch(arr,searchValue)
    print(ans)

main()