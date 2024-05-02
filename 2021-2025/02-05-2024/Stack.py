stack = []

# append() method is the push for stack

stack.append(19)
stack.append(34)
stack.append(67)
print(stack)
poppedElement = stack.pop()
print(poppedElement,"popped element")
print(stack)
print(stack[-1],"top pf stack")
print(len(stack),"size")