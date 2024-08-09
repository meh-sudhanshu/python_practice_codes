



def getQuantityOfWaterThatsTrapped(arr):
    n = len(arr)
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]

    for i in range(n):
        if i == 0:
            left[i] = arr[i]
        else:
            left[i] = max(arr[i],left[i-1])

    for i in range(n-1,-1,-1):
        if i == n-1:
            right[i] = arr[i]
        else:
            right[i] = max(arr[i],right[i+1])

    ans = 0
    for i in range(n):
        currentTrappedWater = min(left[i],right[i]) - arr[i]
        if currentTrappedWater > 0:
            ans+=currentTrappedWater
    return ans





def main():
    arr = [3,2,9,5,1,3,2,6]
    ans = getQuantityOfWaterThatsTrapped(arr)
    print(ans)

main()