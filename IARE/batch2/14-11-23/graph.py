
def printGraphOfMatrix(graph):
    for row in graph:
        for val in row:
            print(val,end=" ")
        print()


def printGraphOfList(graph):
    for node in graph:
        for edge in node:
            print(edge,end=" ")
        print()




def buildGraphUsingMartrix(edges,n):
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for edge in edges:
        src = edge[0]
        des = edge[1]
        wt = edge[2]
        graph[src][des] = wt
        graph[des][src] = wt

    return graph


def buildGraphUsingList(edges,n):
    graph = [[] for i in range(n+1)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        wt = edge[2]
        graph[src].append([src,des,wt])
        graph[des].append([des,src,wt])
    return graph



def isPathExist(graph,src,des,visited):
    if src == des:
        return True
    visited.append(src)
    for edge in graph[src]:
        nbr = edge[1]
        if nbr not in visited:
            visited.append(nbr)
            flag = isPathExist(graph,nbr,des,visited)
            if flag == True:
                return True
    return False

def printAllPaths(graph,src,des,psf,visited):
    if src == des:
        psf+=str(src)
        print(psf)
        return
    psf+=str(src)
    visited[src] = True
    for edge in graph[src]:
        nbr = edge[1]
        if visited[nbr] == False:
            printAllPaths(graph,nbr,des,psf,visited)
    visited[src] = False
    
longestPath, shortestPath = "",""
maximumWeightPath, minimumWeightPath = float('-inf'), float('inf')

def multiSolver(graph,src,des,psf,visited,wsf):
    global longestPath, shortestPath, maximumWeightPath, minimumWeightPath
    if src == des:
        psf+=str(src)
        if len(psf) > len(longestPath):
            longestPath = psf
        if wsf > maximumWeightPath:
            maximumWeightPath = wsf
        if wsf < minimumWeightPath:
            minimumWeightPath = wsf
        if len(psf) < len(shortestPath) or len(shortestPath) == 0:
            shortestPath = psf
        return
    psf+=str(src)
    visited[src] = True
    for edge in graph[src]:
        nbr = edge[1]
        if visited[nbr] == False:
            multiSolver(graph,nbr,des,psf,visited,wsf+edge[2])
        
    visited[src] = False


def isGraphConnectedOrDisconnected(graph,n):
    src = 1
    for i in range(1,n+1):
        flag = isPathExist(graph,src,i,[])
        if flag == False:
            return "Disconnected"
    return "connected"





def isCentric(graph,n):
    for node in graph:
        if len(graph[node]) == n-1:
            return True
    return False



n = 8
visited = [False for i in range(n+1)]
edges = [[1,2,10],[1,4,8],[2,3,7],[4,3,10],[6,5,10],[6,7,23],[7,8,56],[5,8,78]]

# graphUsingMatrix = buildGraphUsingMartrix(edges,n)
# printGraphOfMatrix(graphUsingMatrix)


graph = buildGraphUsingList(edges,n)
#printGraphOfList(graph)

#print(isPathExist(graph,1,6,[]))

#printAllPaths(graph,1,7,"",visited)
#visited = [False for i in range(n+1)]
#multiSolver(graph,1,2,"",visited,0)
#print(longestPath,shortestPath,maximumWeightPath,minimumWeightPath)

print(isGraphConnectedOrDisconnected(graph,n))



