

def getMinimumOperation(arr):
    wholeXor = 0
    isAnsPossible  = -1
    ans = float('+inf')
    for e in arr:
        wholeXor = wholeXor ^ e
    for e in arr:
        exceptThisElementXor = wholeXor ^ e
        if exceptThisElementXor > e:
            isAnsPossible = 1
            currAns = exceptThisElementXor - e
            if currAns < ans:
                ans = currAns
    if isAnsPossible == -1:
        return -1
    return ans
