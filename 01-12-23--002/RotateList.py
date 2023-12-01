

def rotateList(head,k):
    temp, stack, queue, count = head, [], [], 1
    while temp is not None:
        if count < k:
            queue.append(temp.value)
            temp = temp.next
        else:
            stack.append(temp.value)
            temp = temp.next
        count+=1 
    temp = head
    while len(stack) > 0:
        temp.val = stack.pop()
        temp = temp.next
    while len(queue) > 0:
        temp.val = queue.pop(0)
        temp = temp.next

    return head