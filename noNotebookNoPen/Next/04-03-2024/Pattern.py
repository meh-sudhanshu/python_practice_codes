def pattern1(n):
    for i in range(1,n+1):
        j = 1
        ch = 'A'
        while j<=i:
            j+=1
            print(ch,end=" ")
            ch = chr(ord(ch)+1)
            if ch == 'Z':
                ch = 'A'
        print()

def pattern2(n):
    countOfChar = 0
    for i in range(1,n+1):
        j = 1
        ch = 'A'
        for k in range(countOfChar):
            print(" ",end=" ")
        while j<=i:
            j+=1
            print(ch,end=" ")
            countOfChar+=1
            ch = chr(ord(ch)+1)
            if ch == 'Z':
                ch = 'A'
        print()
def pattern3(n):
    space = n-1
    char = 1
    for i in range(n):
        ch = 'A'
        for j in range(space):
            print(" ",end=" ")
        for j in range(char):
            print(ch,end=" ")
            ch = chr(ord(ch)+1)
        print()
        char+=2
        space-=1


pattern3(4)