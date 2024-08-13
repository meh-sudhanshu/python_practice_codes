
def buildGraph(edges,n):
    graph = [[] for i in range(n)]

    for i in range(len(edges)):
        edge = edges[i]
        src = i
        nbr = edge[0]
        wt = edge[1]

        graph[src].append([nbr,wt])
        graph[nbr].append([src,wt])

    return graph




def main():
    edges = [[0,1,2],[1,2,2],[1,3,3],[3,4,10],[4,5,6],[5,7,3],[4,6,18],[6,7,-5]]
    n = 8

    graph = buildGraph(edges,n)
    print(graph)

main()