def bfs(graph,src):
    lookupMap = {}
    queue = []
    queue.append([src,str(src)])
    while len(queue) != 0:
        curr = queue.pop(0)
        cd = curr[0]
        psf = curr[1]
        lookupMap[cd] = 1
        print(cd,psf)
        nbrs = graph[cd]
        for i in range(len(nbrs)):
            if nbrs[i] != 0 and i not in lookupMap:
                queue.append([i,psf+"->"+str(i)])


def buildGraph(edges,n):
    graph = [[0 for i in range(n)] for j in range(n)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        graph[src][des] = 1
        graph[des][src] = 1
    return graph


def main():
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7]]
    n = 8
    graph = buildGraph(edges,n)
    src = 1
    bfs(graph,src)

main()