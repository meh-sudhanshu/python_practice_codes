

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
        wt = edge[2]

        graph[src][des] = wt

    return graph










def printGraph(graph):
    for row in graph:
        for e in row:
            print(e,end=" ")
        print()





def main():
    n = 8
    edges = [[0,1,3],[0,3,2],[1,3,2],[1,2,5],[2,3,4],[2,4,6],[3,4,40],[4,5,3],[5,6,8],
        [5,7,7],[6,7,2]
    ]

    graph = buildGraph(edges,n)
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    #printGraph(graph)

    multiSolver(graph,src,des,visited,str(src),0)
    print(maxCost," max cost ")
    print(minCost, "min cost")
    print(smallestPath, "smallest path")
    print(largestPath, "largest path")

main()