
def getMinimumNumberOfOps(arr):
    wholeXor = 0
    for e in arr : wholeXor = wholeXor ^ e
    ans = float('+inf')
    for e in arr:
        wholeXorExceptE = wholeXor ^ e
        if wholeXorExceptE > e:
            continue
        else:
            currAns = e-wholeXorExceptE
            if currAns < ans:
                ans = currAns
    if ans == float("+inf"):
        return -1
    return ans



def main():
    arr = [3,9,8,17,12]
    ans = getMinimumNumberOfOps(arr)
    print(ans)
main()