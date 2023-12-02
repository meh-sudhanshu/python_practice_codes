

def rotateList(head,k):
    stack = []
    queue = []
    counter = 0  
    temp = head
    while temp :
        if counter < k:
            queue.append(temp.value)
        else:
            stack.append(temp.value)
        counter+=1
        temp = temp.next
    temp = head
    while stack:
        temp.value = stack.pop()
        temp = temp.next
    while queue:
        temp.value = queue.pop(0)
        temp = temp.next

    return head


def getLength(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count

def getMedian(head):
    temp = head
    lenght = getLength(head)
    k = lenght//2 - 1
    while k != 0:
        temp = temp.next 
    if lenght % 2 == 1:
        return temp.value
    return (temp.value+temp.next.value)//2

