

def isPairExist(arr,target):
    arr.sort() #nlogn
    i,j = 0,len(arr)-1
    while i < j: #n
        _sum = arr[i]+arr[j]
        if _sum == target:
            return True
        if _sum > target:
            j = j -1
        if _sum < target:
            i = i+1
    return False
        




def main():
    arr = [3,4,25,-3,-6,34,76,12,-12]
    target = 90
    ans = isPairExist(arr,target)
    print(ans)
main()