


def isPairExist(arr,target):
    arr.sort()
    i = 0
    j = len(arr)-1

    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] < target: i+=1
        if arr[i]+arr[j] > target: j-=1

    return False





def main():
    arr = [3,-1,-5,9,12,13,8,6,5,-6,9]
    target = 11
    ans = isPairExist(arr,target)
    print(ans)

main()