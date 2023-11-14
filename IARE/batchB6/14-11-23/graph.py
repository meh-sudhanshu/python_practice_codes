
def buildGraphWithMatrix(edges,n):
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        wt = edge[2]
        graph[src][des] = wt
        graph[des][src] = wt

    return graph

def printMatrixGraph(graph):
    for row in graph:
        for val in row:
            print(val,end=" ")
        print()

def printListGraph(graph):
    for node in graph:
        for nbr in node:
            print(nbr[2],end=" ")
        print()


def buildGraphWithList(edges,n):
    graph = [[] for i in range(n+1)]

    for edge in edges:
        src = edge[0]
        des = edge[1]
        wt = edge[2]
        graph[src].append([src,des,wt])
        graph[des].append([des,src,wt])

    return graph


def hasPath(graph,src,des,visited):
    if src == des:
        return True
    for edge in graph[src]:
        if visited[edge[1]] == False:
            visited[edge[1]] = True
            flag = hasPath(graph,edge[1],des,visited)
            if flag == True:
                return True
    return False 


def isGraphConnected(graph,n):
    src = 1
    for i in range(1,n+1):
        flag = hasPath(graph,src,i,[False for i in range(n+1)])
        if flag == False:
            return "Disconnected"
    return "Connected"

def printAllPath(graph,src,des,psf,visited):
    if src == des:
        psf+=str(src)
        print(psf)
        return
    psf+=str(src)
    visited[src] = True
    for edge in graph[src]:
        if visited[edge[1]] == False:
            printAllPath(graph,edge[1],des,psf,visited) 
    visited[src] = False


n = 8
edges = [[1,2,4],[1,4,10],
         [2,3,56],[2,5,78], 
         [4,3,24],[5,8,13],
         [5,6,78],[8,7,23],
         [6,7,45]]

visited = [False for i in range(n+1)]
graph = buildGraphWithList(edges,n)
#graphUsingMatrix = buildGraphWithMatrix(edges,n)

# printListGraph(graphUsingList)
# printMatrixGraph(graphUsingMatrix)
print(hasPath(graph,1,8,visited))
print(isGraphConnected(graph,n))

printAllPath(graph,1,8,"",[False for i in range(n+1)])