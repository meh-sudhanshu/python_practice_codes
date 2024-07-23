

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def createList(self,arr):
        head = None
        temp = None
        for i in range(len(arr)):
            if i == 0:
                head = Node(arr[i])
                temp = head
            else:
                temp.next = Node(arr[i])
                temp = temp.next
        return head

    def printList(self,head):
        while head != None:
            print(head.val,end=" ")
            head = head.next


def main():
    arr = [2,3,9,13,45,67]
    myListOperator = LinkedList()
    head = myListOperator.createList(arr)
    myListOperator.printList(head)

main()
