
minWeight, maxWeight = float('+inf'), float('-inf')

longestPath, shortestPath = "", ""


def buildGraph(n,edges):
    adjacencyMatrix = [[0 for i in range(n)] for j in range(n)]
    #matrix = [0 for i in range(n)]*n
    for edge in  edges:
        src = edge[0]
        des = edge[1]
        wt = edge[2]
        adjacencyMatrix[src][des] = wt
        adjacencyMatrix[des][src] = wt
    return adjacencyMatrix
  
def printGraph(graph):
    for row in graph:
        for value in row:
            print(value,end=" ")
        print()

def isPathExist(src,des,graph,visited):
    if src == des and len(visited)>1:
        return True
    info = graph[src]
    for i in range(len(info)):
        if info[i] != 0:
            if i not in visited:
                visited.append(i)
                flag = isPathExist(i,des,graph,visited)
                if flag == True:
                    return True
    return False

def printAllPaths(src,des,graph,visited,psf,wsf):
    global minWeight, maxWeight, longestPath, shortestPath
    if src == des:
        print(psf,"psfff")
        if len(psf)>len(longestPath) or len(longestPath) == 0:
            longestPath = psf
        if len(shortestPath) == 0 or len(psf) < len(shortestPath):
            shortestPath = psf
        if wsf > maxWeight: maxWeight = wsf
        if wsf < minWeight : minWeight = wsf
    info = graph[src]
    for i in range(len(info)):
        if info[i] != 0:
            if i not in visited:
                visited.append(i)
                printAllPaths(i,des,graph,visited,psf+str(i),wsf+info[i])
                visited.remove(i)
                # if flag == True:
                #     return True

def isCyclic(graph,n,visited):
    for i in range(n):
        flag = isPathExist(i,i,graph,visited )
        if flag == True:
            return True
    return False
    
edges = [[0,2,8],[0,1,-9],[1,3,7],[4,5,56],[5,6,1],
            [6,7,69],[7,4,67],[3,2,65],[3,4,8]]

#nbr = [[1,2],[3],[],[4,2],[5],[6],[7],[4]]

nodes = 8
graph = buildGraph(nodes,edges)
#printGraph(graph)
visited = []
src = 0
des = 2
visited.append(src)
# #print(isPathExist(src,des,graph,visited))
# printAllPaths(src,des,graph,visited,str(src),0)

# print(longestPath,"longest")
# print(shortestPath,"shortest")
# print(minWeight,"min-weight")
# print(maxWeight ,"max-weight")

print(isCyclic(graph,nodes,visited))

