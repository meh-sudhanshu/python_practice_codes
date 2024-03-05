

def binarySearch(arr,ele):
    low, high = 0, len(arr)-1
    while low < high:
        mid = (low+high) // 2
        if arr[mid] == ele:
            return True
        if arr[mid] > ele:
            high = mid-1
        else:
            low = mid+1
    return False

        
    
arr = [89,23,-23,-45,98,3,6,78,98,-22,-54,76]
arr.sort()
print(binarySearch(arr,78))
# for i in range(100):
#     print(binarySearch(arr,i+1))