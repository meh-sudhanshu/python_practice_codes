def build_graph(number_of_vertices):
    graph = [[] for i in range(number_of_vertices)]

    graph[0].append([0,1,10])
    graph[0].append([0,2,10])

    graph[1].append([1,3,10])
    graph[1].append([1,0,10])
    graph[1].append([1,4,10])

    graph[2].append([2,3,10])
    graph[2].append([2,0,10])

    graph[3].append([3,2,10])
    graph[3].append([3,1,10])

    graph[4].append([4,7,10])
    graph[4].append([4,5,10])
    graph[4].append([4,1,10])

    graph[5].append([5,4,10])
    graph[5].append([5,6,10])

    graph[6].append([6,7,10])
    graph[6].append([6,5,10])

    graph[7].append([7,6,10])
    graph[7].append([7,4,10])

    return graph


def print_graph(graph):
    for vertices in graph:
        for edge in vertices:
            print(edge,end=" ")
        print()

def has_path(graph, src , des , visited):
    if src == des:
        return True
    visited[src] = True
    for edge in graph[src]:
        if visited[edge[1]] == False:
            value = has_path(graph,edge[1],des,visited)
            if value == True:
                return True
    return False


def print_all_path(graph,src,des,psf,visited):
    if src == des:
        psf += str(src)
        print(psf)
        return
    psf+=str(src)
    visited[src] = True
    for edge in graph[src]:
        if visited[edge[1]] == False:
            print_all_path(graph,edge[1],des,psf,visited)
    visited[src] = False



def main():
    number_of_vertices = 8
    graph = build_graph(number_of_vertices)
    #print(graph)
    #print_graph(graph)
    visited = [False for i in range(number_of_vertices)]
    #print(has_path(graph,0,3,visited))
    print_all_path(graph,0,6,"",visited)

main()





