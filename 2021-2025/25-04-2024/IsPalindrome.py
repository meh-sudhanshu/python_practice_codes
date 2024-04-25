def isPalindrome(_str):
    i ,j = 0, len(_str)-1
    while i<j:
        if _str[i] != _str[j]:
            return False
        i+=1
        j-=1
    return True

print(isPalindrome("malayhgvhgalam"))