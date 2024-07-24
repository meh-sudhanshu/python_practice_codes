

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




def main():
    edges = [[0,1],[0,2],[1,3],[2,3],[4,5],[4,6],[5,7],[6,7]]
    n = 8
    graph = buildGraph(edges,n)
    #printGraph(graph)
    src = 3
    des = 5
    visited = [0 for i in range(n)]
    ans = hasPath(graph,src,des,visited)
    print(ans)

main()