

def buildGraph(edges,n):
    graph = [[] for i in range(n)]

    for edge in edges:
        src1 = edge[0]
        src2 = edge[1]

        des1 = edge
        des2 = edge[::-1]

        graph[src1].append(des1)
        graph[src2].append(des2)

    return graph





def main():
    edges = [[0,1],[0,2],[1,3],[3,2],[3,4],[4,6],[4,5],[5,7],[6,7]]
    n = 8
    graph = buildGraph(edges,n)
    print(graph)


main()