def isPalindromeIteratively(_str):
    i,j = 0, len(_str)-1
    while i < j:
        if _str[i] != _str[j]:
            return False
        i+=1
        j-=1
    return True

def isPalindrome(_str):
    if len(_str) == 0 or len(_str) == 1:
        return True
    if _str[0] != _str[-1]:
        return False
    subStr = _str[1:len(_str)-1]
    return isPalindrome(subStr)