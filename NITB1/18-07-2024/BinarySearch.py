
def binarySearch(ele,arr):
    i,j = 0, len(arr)-1
    while i<j:
        mid = (i+j)//2
        if arr[mid] == ele: return True
        if arr[mid] > ele: j = mid-1
        if arr[mid] < ele: i = mid+1
    return False

def main():
    arr = [3,2,6,7,8,9,12,14,56,-78,-98]
    queries = [3,3,7,8,2,56,76,876,984,12,34]
    arr.sort()
    for e in queries:
        print(binarySearch(e,arr),end=" ")
main()