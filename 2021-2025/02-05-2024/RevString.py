def reverse(_str):
    stack = []
    ans = ""
    for i in range(len(_str)):
        stack.append(_str[i])
    for i in range(len(_str)):
        ans+=stack.pop()
    return ans
_str = "sudhanshu"
ans = reverse(_str)
print(ans)