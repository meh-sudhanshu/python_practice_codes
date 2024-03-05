

stack = []
stack.append(2)
stack.append(8)
stack.append(9)
stack.append(-3)
stack.append(5)
stack.append(12)
pointer = 3
st1 = []
st2 = []
top = len(stack)-pointer
while top!=0:
    st1.append(stack.pop())
    top-=1
while len(stack)!=0:
    st2.append(stack.pop())
while len(st1)!=0:
    stack.append(st1.pop())
while len(st2)!=0:
    stack.append(st2.pop())

print(stack)

# ((()))

# }  {  ]  [   )  {