

def isValid(str):
    st = []
    for ch in str:
        if ch == '(' or ch=="{" or ch == "[":
            st.append(ch)
        elif ch == '}' and st[-1]!="{":
            return False
        elif ch == ']' and st[-1]!="[":
            return False
        elif ch == ')' and st[-1]!="(":
            return False
        elif ch == ")" and st[-1] =="(":
            st.pop()
        elif ch == "]" and st[-1] =="[":
            st.pop()
        elif ch == "}" and st[-1] =="{":
            st.pop()
    return len(st) == 0

print(isValid("[[{{(()}]]"))
        
