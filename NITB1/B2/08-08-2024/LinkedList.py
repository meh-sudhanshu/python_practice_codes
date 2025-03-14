


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def generateList(self,arr):
        head = None
        temp = None
        for e in arr:
            if head == None:
                head = Node(e)
                temp = head
            else:
                temp.next = Node(e)
                temp = temp.next
        return head

    def printList(self,head):
        while head is not None:
            print(head.data,end=" ")
            head = head.next
        print()


    def reverseList(self,head):
        st = []
        temp = head
        while temp is not None:
            st.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            temp.data = st.pop()
            temp = temp.next
        return head
        

    




def main():
    arr = [2,5,7,45,35,38]
    myListOperator = LinkedList()
    head = myListOperator.generateList(arr)
    myListOperator.printList(head)
    head = myListOperator.reverseList(head)
    myListOperator.printList(head)

main()