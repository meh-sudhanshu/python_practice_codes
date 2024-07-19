

def buildMatrix(_str,dp):
    si,ei = 0,0
    n = len(dp)
    count = 0
    k = 3
    kCount = 0
    largest = ""
    smallest = ""
    while ei < n:
        ce = ei
        while ce < n:
            if si == ce:
                dp[si][ce] = 1
                count+=1
                largest = _str[si:ce+1]
                if abs(si-ce) == k-1:
                    kCount+=1
            elif abs(ce-si) <= 2:
                if _str[si] == _str[ce]:
                    dp[si][ce] = 1
                    count+=1
                    largest = _str[si:ce+1]
                    if smallest == "":
                        smallest = _str[si:ce+1]
                    if abs(si-ce) == k-1:
                        kCount+=1
            else:
                if _str[si] == _str[ce] and dp[si+1][ce-1] == 1:
                    dp[si][ce] = 1
                    count+=1
                    largest = _str[si:ce+1]
                    if smallest == "":
                        smallest = _str[si:ce+1]
                    if abs(si-ce) == k-1:
                        kCount+=1

            si+=1
            ce+=1
        si = 0
        ei+=1
    return [dp,count,largest,smallest,kCount]

def main():
    _str = "abcdcbcbaudbz"
    n = len(_str)
    dp = [[0 for i in range(n)] for j in range(n)]
    ans = buildMatrix(_str,dp)
    dp = ans[0]
    totalNumberOfPalindromicSubstring = ans[1]
    largest = ans[2]
    smallest = ans[3]
    kCount = ans[4]
    print(totalNumberOfPalindromicSubstring)
    print(largest)
    print(smallest)
    print(kCount)
main()