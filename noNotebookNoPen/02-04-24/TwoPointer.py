def isPairExist(arr,target):
    arr.sort()
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] > target: j-=1
        if arr[i]+arr[j] < target: i+=1
    return False 

def main():
    arr = [-3,5,2,1,0,-6,9,5]
    target = 7
    ans = isPairExist(arr,target)
    print(ans)
main()