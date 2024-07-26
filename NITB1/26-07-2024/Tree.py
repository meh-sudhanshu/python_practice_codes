

class Node:
    def __init__(self,data):
        self.data = data
        self.index = 1
        self.left = None
        self.right = None

class Tree:
    def buildTree(self,arr):
        st = []
        node = Node(arr[0])
        st.append(node)
        i = 1
        while len(st) > 0 and i<len(arr):
            newNode = Node(arr[i])
            peekNode = st[-1]
            if peekNode.index == 1:
                peekNode.left = newNode
                peekNode.index = 2
            elif peekNode.index == 2:
                peekNode.right = newNode
                peekNode = 3
            else:
                st.pop()
            st.append(newNode)
            i+=1 
        return node

    def printTree(self,node):
        if node == None:
            print(None,end=" ")
            return 
        else:
            print(node.data,end=" ")
            self.printTree(node.left)
            self.printTree(node.right)




def main():
    arr = [10,26,33,None,4,None,None,None,3,55,None,None,6,7,None,None,None]
    treeOperator = Tree()
    tree = treeOperator.buildTree(arr)
    treeOperator.printTree(tree)

main()