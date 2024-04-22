def isPalindrome(_str):
    if len(_str) <=1: return True
    if _str[0] != _str[-1]: return False
    subStr = _str[1:len(_str)-1]
    return isPalindrome(subStr)
print(isPalindrome("malaydsalam"))
