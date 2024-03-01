
def buildGraph(n,edges):
    adjacencyMatrix = [[0 for i in range(n)] for j in range(n)]
    #matrix = [0 for i in range(n)]*n
    for edge in  edges:
        src = edge[0]
        des = edge[1]
        adjacencyMatrix[src][des] = 1
        adjacencyMatrix[des][src] = 1
    return adjacencyMatrix

def printGraph(graph):
    for row in graph:
        for value in row:
            print(value,end=" ")
        print()

def isPathExist(src,des,graph,visited):
    if src == des:
        return True
    info = graph[src]
    for i in range(len(info)):
        if info[i] == 1:
            if i not in visited:
                visited.append(i)
                flag = isPathExist(i,des,graph,visited)
                if flag == True:
                    return True
    return False

def printAllPaths(src,des,graph,visited,psf):
    if src == des:
        print(psf)
    info = graph[src]
    for i in range(len(info)):
        if info[i] == 1:
            if i not in visited:
                visited.append(i)
                printAllPaths(i,des,graph,visited,psf+str(i))
                visited.remove(i)
                # if flag == True:
                #     return True
    
edges = [[0,2],[0,1],[1,3],[4,5],[5,6],
            [6,7],[7,4],[3,2],[3,4]]

#nbr = [[1,2],[3],[],[4,2],[5],[6],[7],[4]]

nodes = 8
graph = buildGraph(nodes,edges)
#printGraph(graph)
visited = []
src = 0
des = 6
visited.append(src)
#print(isPathExist(src,des,graph,visited))
printAllPaths(src,des,graph,visited,str(src))


