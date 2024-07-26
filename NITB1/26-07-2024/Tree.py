

class Node:
    def __init__(self,data):
        self.data = data
        self.index = 1
        self.left = None
        self.right = None

class Tree:
    def buildTree(arr):
        st = []
        node = Node(arr[0])
        st.append(node)
        i = 1
        while len(st) > 0:
            if arr[i] == None:
                continue
            newNode = Node(arr[i])
            peekNode = st[-1]
            if peekNode.index == 1:
                peekNode.left = newNode
                peekNode.index+=1
            elif peekNode.index == 2:
                peekNode.right = newNode
                peekNode.index+=1
            else:
                st.pop()
            i+=1
        
        return node




def main():
    arr = [1,2,3,None,4,None,None,None,3,5,None,None,6,7,None,None,None]
    tree = buildTree(arr)