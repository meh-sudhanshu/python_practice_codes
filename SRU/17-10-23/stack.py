stack = []

stack.append(10)
stack.append(23)
stack.append(45)

print(stack.pop())
print(stack.pop())

if len(stack) >=1:
    print(stack[-1])
else:
    print("stack is empty")
