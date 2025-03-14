


def getMaximumSum(arr):
    ans = float("-inf")
    n = len(arr)
    trainSum = 0
    for i in range(n):
        if trainSum < 0:
            trainSum = 0
        trainSum+=arr[i]
        ans = max(trainSum,ans)
       
    return max(ans,trainSum)




def main():
    arr = [2,3,-8,14,3,-15,6,7,-2,8,-13,18]
    ans = getMaximumSum(arr)
    print(ans)

main()