class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.temp = None
    def create_list(self):
        for i in range(11):
            new_node = Node(i)
            if self.start is None:
                self.start = new_node
                self.temp = self.start
            else:
                self.temp.next = new_node
                self.temp = self.temp.next
        return self.start
    def print_list(self):
        self.temp = self.start
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
        print()
    def reverse_list(self):
        self.temp = self.start
        arr = []
        while self.temp is not None:
            arr.append(self.temp.data)
            self.temp = self.temp.next
        arr = arr[::-1]
        self.temp = self.start
        i = 0
        #print("arr",arr)
        while self.temp is not None:
            self.temp.data = arr[i]
            i+=1
            self.temp = self.temp.next
        


    # def find_median(self):
    #     self.temp = self.start
    #     print("self.temp-check1",self.temp)
    #     length = self.find_length()
    #     counter = length//2
    #     counter-=1
    #     print("counter",counter)
    #     i = 1
    #     while i!= counter:
    #         print(i,end=" ")
    #         self.temp = self.temp.next
    #         i+=1
    #     print("self.temp-check2",self.temp)
    #     if length % 2 == 1 and self.temp is not None:
    #         return self.temp.next.data
    #     elif self.temp is not None and self.temp.next is not None:
    #         return (self.temp.data + self.temp.next.data) // 2

    def find_length(self):
        self.temp = self.start
        ans = 0
        while self.temp is not None:
            ans+=1
            self.temp = self.temp.next
        return ans







object_ = LinkedList()
start = object_.create_list()
object_.print_list()
object_.reverse_list()
object_.print_list()



#object_.print_list()
#object_.print_list()


# length = object_.find_length()
# print(length)

#median = object_.find_median()
#print("median ",median)