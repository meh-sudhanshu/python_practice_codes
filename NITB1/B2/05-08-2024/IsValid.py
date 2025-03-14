


def isValid(_str):
    stack = []

    for ch in _str:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0: return False

            poppedChar = stack.pop()

            if ch == ')'  and poppedChar != '(': return False
            if ch == ']'  and poppedChar != '[': return False
            if ch == '}'  and poppedChar != '{': return False

    return len(stack) == 0






def main():
    _str = "[[[{{()()}()}]]]"

    ans = isValid(_str)
    print(ans)

main()