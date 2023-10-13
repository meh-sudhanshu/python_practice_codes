class Node:
    # def __new__(self,data):
    #     print("inside new")
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    def append_node(self,data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()


my_list = LinkedList()
for i in range(11):
    my_list.append_node(i)
my_list.print_list()






        

