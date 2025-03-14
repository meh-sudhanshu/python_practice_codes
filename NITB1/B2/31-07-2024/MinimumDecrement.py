def getMinDecrement(arr):
    allXor = 0
    for e in arr: allXor = allXor ^ e

    ans = -1

    for e in arr:
        allXorExceptE = allXor ^ e

        if allXorExceptE <= e:
            currAns = e - allXorExceptE
            if ans == -1 or currAns < ans:
                ans = currAns
    
    return ans





def main():
    arr = [7,3,8,9,5,12]
    ans = getMinDecrement(arr)
    print(ans)

main()