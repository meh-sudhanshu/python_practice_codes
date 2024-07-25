
largestPath = ""
smallestPath = ""


def buildGraph(edges,n):
    graph = [[0 for i in range(n)] for j in range(n)]
    for edge in edges:
        src = edge[0]
        des = edge[1]

        graph[src][des] = 1
        graph[des][src] = 1
    return graph

def printGraph(graph):
    for row in graph:
        for e in row:
            print(e,end=" ")
        print()


def hasPath(graph,src,des,visited):
    if src == des:
        return True
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1:
            if visited[i] == 0:
                visited[i] = 1
                ans = hasPath(graph,i,des,visited)
                if ans == True:
                    return True
    return False

def printAllPath(graph,src,des,visited,psf):
    global largestPath
    global smallestPath
    if src == des:
        if len(psf) > len(largestPath):
            largestPath = psf
        if smallestPath == "" or len(psf) < len(smallestPath):
            smallestPath = psf
        #print(psf)
        return
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1:
            if visited[i] == 0:
                visited[i] = 1
                printAllPath(graph,i,des,visited,
                    str(src)+"->"+str(i) if psf == "" else psf+"->"+str(i),
                )
                visited[i] = 0

def buildGraphWithAdjacencyList(edges,n):
    graph = [[] for i in range(n)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        wt  = edge[2]
        graph[src].append([src,des,wt])
        # graph[des].append([des,src,wt])
    return graph

def printGraphInAdjacencyList(graph):
    for node in graph:
        for edges in node:
            print(edges ,end=" ")


def hasPath(graph,src,des,visited):
    if src == des:
        return True
    nbrs = graph[src]
    for nbr in nbrs:
        if visited[nbr[1]] == 0:
            visited[nbr[1]] = 1
            ans = hasPath(graph,nbr[1],des,visited)
            if ans == True:
                return True
    return False
    
def bfs(graph,src,visited,queue):
    while len(queue) > 0:
        popepedElement = queue.pop(0)
        currentNode = popepedElement[0]
        psf = popepedElement[1]
        visited[currentNode] = 1
        print(currentNode,"->",psf)
        nbrs = graph[currentNode]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                queue.append([i,psf+str(i)])

def getCurrentComponent(graph,src,visited,currentComponent):
    visited[src] = 1
    currentComponent.append(src)
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1 and visited[i] == 0:
            getCurrentComponent(graph,i,visited,currentComponent)
    
def getAllCompoents(graph,n):
    visited = [0 for i in range(n)]
    ans = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            currentComponent = []
            getCurrentComponent(graph,i,visited,currentComponent)
            ans.append(currentComponent)
    return ans

def isCyclic(graph,n):
    sc = -1
    queue = []
    queue.append([0,"0"])
    visited = [0 for i in range(n)]
    while len(queue) > 0:
        popepedElement = queue.pop(0)
        currentNode = popepedElement[0]
        if visited[currentNode] == 1:
            print(popepedElement[1])
            # if sc == -1:
            #     sc = popepedElement[1]+str(currentNode)
            # elif len(popepedElement[1]+str(currentNode)) < len(sc):
            #     sc =  popepedElement[1]+str(currentNode)
        psf = popepedElement[1]
        visited[currentNode] = 1
        #print(currentNode,"->",psf)
        nbrs = graph[currentNode]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                queue.append([i,psf+str(i)])

    return sc
def expandNode(graph,i,j,visited,n):
    if i>=n or i<0 or j>=n or j<0 or graph[i][j] == 0 or visited[i][j] == 1:
        return
    visited[i][j] = 1

    expandNode(graph,i+1,j,visited,n)
    expandNode(graph,i-1,j,visited,n)
    expandNode(graph,i,j+1,visited,n)
    expandNode(graph,i,j-1,visited,n)



        
def getNumberOfIsland(graph,n):
    count = 0
    visited = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                expandNode(graph,i,j,visited,n)
                count+=1
    return count



def main():
    global smallestPath
    global largestPath
    edges = [[0,1],[0,2],[2,1],[3,6],[3,4],[6,5],[4,5],[7,8],[9,10],[9,11],[10,11]]
    n = 12
    graph = buildGraph(edges,n)
    # #printGraph(graph)
    src = 0
    visited = [0 for i in range(n)]
    queue = [[0,"0"]]
    #bfs(graph,src,visited,queue)
    # visited[src] = 1
    # #ans = hasPath(graph,src,des,visited)
    # #print(ans)
    # printAllPath(graph,src,des,visited,"")
    # print(smallestPath)
    # print(largestPath)
    #graph = buildGraphWithAdjacencyList(edges,n)
    #printGraphInAdjacencyList(graph)
    #ans = hasPath(graph,src,des,visited)
    #print(ans)
    #ans = isCyclic(graph,n)
    #print(ans)
    matrix =  [[1,1,1,0,0,1],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,1,1,1,0,1],[1,0,0,1,1,0],
        [0,0,0,1,1,0]
    ]
    # ans = getAllCompoents(graph,n)
    # print(ans)
    ans = getNumberOfIsland(matrix,6)
    print(ans)
main()