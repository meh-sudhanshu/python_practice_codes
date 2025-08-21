

def isPairExist(arr,target):
    arr.sort()
    i,j = 0, len(arr)-1
    while i < j:
        sum = arr[i]+arr[j]
        if sum == target: return True
        if sum > target: j-=1
        if sum < target: i+=1
    return False


def main():
    arr = [-3,0,4,2,6,-9,3,-5,4]
    target = 800
    ans = isPairExist(arr,target)
    print(ans)
main()