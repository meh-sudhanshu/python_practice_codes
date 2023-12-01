def main():
    arr = [5,7,8]
    wholeXor = 0
    ans = float('+inf')
    for e in arr:
        wholeXor = wholeXor^e
    isAnsPossible = -1  
    for e in arr:
        exceptThisElementXor = wholeXor^e
        if e > exceptThisElementXor:
            isAnsPossible = 1
            currentAns = e - exceptThisElementXor
            if currentAns < ans:
                ans = currentAns
    if isAnsPossible == 1:
        print(ans)
    else:
        print(-1)




main()