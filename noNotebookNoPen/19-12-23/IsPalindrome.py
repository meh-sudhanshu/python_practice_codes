def isPalindrome(str):
    if len(str) == 0 or len(str)==1:
        return True
    if str[0] != str[-1]:
        return False
    subStr = str[1:len(str)-1]
    return isPalindrome(subStr)

print(isPalindrome("MadaMcsc"))