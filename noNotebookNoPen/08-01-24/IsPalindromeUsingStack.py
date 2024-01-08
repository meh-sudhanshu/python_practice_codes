

def isPalindrome(string):
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
    for i in range(len(string)):
        if string[i] != stack.pop():
            return False
    return True

print(isPalindrome("MadaMhvhv"))
