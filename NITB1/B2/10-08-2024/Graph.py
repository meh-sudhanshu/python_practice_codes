

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

    printGraph(graph)

main()