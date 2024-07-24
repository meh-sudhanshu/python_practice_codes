
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
    




def main():
    global smallestPath
    global largestPath
    edges = [[0,1],[0,2],[1,3],[3,4],[4,5],[4,6],[5,7],[6,7],[1,5],[2,3]]
    n = 8
    graph = buildGraph(edges,n)
    # #printGraph(graph)
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    # #ans = hasPath(graph,src,des,visited)
    # #print(ans)
    printAllPath(graph,src,des,visited,"")
    print(smallestPath)
    print(largestPath)
    #graph = buildGraphWithAdjacencyList(edges,n)
    #printGraphInAdjacencyList(graph)
    #ans = hasPath(graph,src,des,visited)
    #print(ans)

main()