


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
    printGraph(graph)


main()
