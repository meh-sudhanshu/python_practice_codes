
def printAllPath(graph,src,des,visited,psf):
    if src == des:
        print(psf)
        return
    nbrs = graph[src]

    for i in range(len(nbrs)):
        if nbrs[i] == 1:
            if visited[i] == 0:
                visited[i] = 1
                printAllPath(graph,i,des,visited, psf+"->"+str(i))
                visited[i] = 0
    return False








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




def main():
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[6,7],[5,7]]
    n = 8
    # bidirectional, non-weighted no self cycle graph
    graph = buildGraph(edges,n)
    #printGraph(graph)
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    
    #isPathExist = hasPath(graph,src,des,visited)
    #print(isPathExist)

    printAllPath(graph,src,des,visited,str(src))


main()
