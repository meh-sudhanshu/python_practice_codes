# "(((())))"
# "(()"
# ")(()))(("
# ")("

def isValid(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")" and len(stack) == 0:
            return False
        else:
            stack.pop()
    return len(stack) == 0
print(isValid("((())"))