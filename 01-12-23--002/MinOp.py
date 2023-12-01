

def main():
    arr = [5,7,8]
    wholeXor ,isAnsPossible =0, -1
    for e in arr:  wholeXor = wholeXor^e
    ans = float('+inf')
    for e in arr:
        exceptThisElementXor = wholeXor^e
        if exceptThisElementXor < e:
            isAnsPossible = 1
            currentAns = e - exceptThisElementXor
            if currentAns < ans:
                ans = currentAns
    if isAnsPossible == -1:
        print(-1)
    else:
        print(ans)

main()
