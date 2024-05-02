def isValid(_str):
    stack=[]
    for i in range(len(_str)):
        if _str[i] == '(':
            stack.append("(")
        elif _str[i] == ')' and len(stack) == 0:
            return False
        else: stack.pop()
    return len(stack) == 0