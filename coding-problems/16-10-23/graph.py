
vertices = 6
graph = [[[]] for i in range(vertices)]
graph[0] = [[0,1,3],[0,2,2]]
graph[1] = [[1,0,3],[1,2,5]]
graph[2] = [[2,0,1],[2,1,4]]

graph[3] = [[3,4,3],[3,5,2]]
graph[4] = [[4,3,3],[4,5,5]]
graph[5] = [[5,4,1],[5,3,4]]

visited = [False for i in range(vertices)]

def has_path(graph, src , des , visited):
    if src == des:
        return True
    for neighbour in graph[src]:
        next_neighbour = neighbour[1]
        if visited[next_neighbour] == False:
            visited[next_neighbour] = True
            result = has_path(graph,neighbour[1],des,visited)
            if result == True:
                return True
    return False
    
print(has_path(graph,1,3,visited))

    
    