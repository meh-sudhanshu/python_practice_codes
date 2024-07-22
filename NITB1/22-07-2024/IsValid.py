


def isValid(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        elif s[i] == ')' and st[-1] != '(': return False
        elif s[i] == '}' and st[-1] != '{' : return False
        elif s[i] == ']' and st[-1] != '[' : return False
        else:
            st.pop()

    return len(st) == 0





def main():
    _str = "(((({}[]())))"
    ans = isValid(_str)
    print(ans)

main()