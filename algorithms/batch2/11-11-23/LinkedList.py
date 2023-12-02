
class Node:
    def __init__(self,value) -> None:
        self.next = None
        self.value = value
           



def getLength(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count



def getMedian(head):
    _legth = getLength(head)
    median = 0
    temp = head
    k = (_legth//2 - 1)
    while k != 0:
        temp = temp.next
        k-=1
    if _legth % 2 == 0:
        median = (temp.value + temp.next.value) //2
    else:
        median = temp.value   
    return median


def reverseList(head):
    st = []
    temp = head

    while temp:
        st.append(temp.value)
        temp = temp.next
    
    temp = head
    while temp:
        temp.value = st.pop()
        temp = temp.next


    return head

def addToStart(head,ele):
    temp = Node(ele)
    temp.next = head
    head = temp

    return head




def rotateListAtK(head,k):
    temp = head
    tempK = k
    while tempK != 0:
        temp = temp.next
        tempK-=1
    queue = []
    while temp:
        queue.append(temp.value)
        temp = temp.next
    
    while len(queue) != 0:
        ele = queue.pop(0)
        head = addToStart(head,ele)

    tempK = 2*k - 1
    temp = head
    while tempK != 0:
        temp = temp.next

    temp.next = None

    return head
    
