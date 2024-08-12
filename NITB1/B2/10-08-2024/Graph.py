

maxCost = float("-inf")
minCost = float("+inf")

largestPath = ""
smallestPath = -1



def multiSolver(graph,src,des,visited,psf,csf):
    global maxCost
    global minCost
    global smallestPath
    global largestPath
    if src == des:
        if len(psf) > len(largestPath):
            largestPath = psf
        if smallestPath == -1 or len(psf) < len(smallestPath):
            smallestPath = psf

        if csf > maxCost:
            maxCost = csf
        if csf < minCost:
            minCost = csf
        return
    nbrs = graph[src]

    for i in range(len(nbrs)):
        if nbrs[i] != 0:
            if visited[i] == 0:
                visited[i] = 1
                multiSolver(graph,i,des,visited, psf+"->"+str(i), csf + nbrs[i])
                visited[i] = 0
    return False




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


def bfs(graph,src,visited,queue):
    while len(queue) > 0:
        removedElement = queue.pop(0)
        currentDestination = removedElement[0]
        psf = removedElement[1]
        visited[currentDestination] = 1
        print(str(currentDestination)+"|"+psf)
        nbrs = graph[currentDestination]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                queue.append([i,psf+"->"+str(i)])


def isCyclic(graph,n):
    queue = []
    queue.append([0,"0"])
    visited = [0 for i in range(n)]
    while len(queue) > 0:
        removedElement = queue.pop(0)
        currentDestination = removedElement[0]
        psf = removedElement[1]
        if visited[currentDestination] == 1: 
            return True
        visited[currentDestination] = 1
        #print(str(currentDestination)+"|"+psf)
        nbrs = graph[currentDestination]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                queue.append([i,psf+"->"+str(i)])
    return False


def expandNode(graph,n,src,currComponent,visited):
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1 and visited[i] == 0:
            visited[i] = 1
            currComponent.append(i)
            expandNode(graph,n,i,currComponent,visited)








def getAllComponents(graph,n):
    visited = [0 for i in range(n)]
    ans = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            currComponent = [i]
            expandNode(graph,n,i,currComponent,visited)
            ans.append(currComponent)
    return ans










def main():
    n = 12
    edges = [[0,2],[0,3],[1,3],[4,5],[6,7],[6,8],[8,9],[10,11]]
    

    graph = buildGraph(edges,n)

    queue = [[0,"0"]]
    visited = [0 for i in range(n)]
    src = 0
    #bfs(graph,src,visited,queue)
    # ans = isCyclic(graph,n)
    # print(ans)

    ans = getAllComponents(graph,n)
    print(ans)



    #src = 0
    #des = 7
    #visited = [0 for i in range(n)]
    #visited[src] = 1
    #printGraph(graph)

    #multiSolver(graph,src,des,visited,str(src),0)
    #print(maxCost," max cost ")
    #print(minCost, "min cost")
    # print(smallestPath, "smallest path")
    # print(largestPath, "largest path")

main()