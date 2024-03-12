
def buildGraph(edges,n):
    graph = [[] for i in range(n)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        graph[src].append(des)
    return graph  

edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,7],[7,6],[5,6]]
n = 8
graph = buildGraph(edges)
