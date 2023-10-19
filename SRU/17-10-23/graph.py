from collections import deque

min_weight = float('+inf')
min_weight_path = ""
max_weight = float('-inf')
max_weight_path = ""

threshold_ceil = float('-inf')
threshold_ceil_path = ""
threshold_floor = float('+inf')
threshold_floor_path = ""

components = []



def build_graph(number_of_vertices):

    graph = [[] for i in range(number_of_vertices)]

    graph[0].append([0,1,10])
    graph[0].append([0,2,8])

    graph[1].append([1,0,5])
    graph[1].append([1,3,5])
    graph[1].append([1,4,10])

    graph[2].append([2,3,7])
    graph[2].append([2,0,8])

    graph[3].append([3,2,7])
    graph[3].append([3,1,10])

    graph[4].append([4,7,10])
    graph[4].append([4,5,8])
    graph[4].append([4,1,8])

    graph[5].append([5,4,8])
    graph[5].append([5,6,3])

    graph[6].append([6,5,2])
    graph[6].append([6,7,3])

    graph[7].append([7,6,2])
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

def multi_solver(graph,src,des,psf,wsf,visited,threshold):
    global min_weight
    global min_weight_path
    global max_weight
    global max_weight_path
    global threshold_ceil
    global threshold_floor
    global threshold_ceil_path
    global threshold_floor_path
    # k --> kth largest path according to weight
    # threshold -> path with floor and ceil of threshold
    # largest path from src to des acc to weight
    # smallest path from src to des acc to weight
    if src == des:
        psf += str(src)
        if wsf < min_weight:
            min_weight = wsf
            min_weight_path = psf
        if wsf > max_weight:
            max_weight = wsf
            max_weight_path = psf
        if wsf > threshold and threshold_ceil < wsf:
            threshold_ceil = wsf
            threshold_ceil_path = psf
        if wsf < threshold and threshold_floor > wsf:
            threshold_floor = wsf
            threshold_floor_path = psf        
    psf+=str(src)
    visited[src] = True
    for edge in graph[src]: 
        if visited[edge[1]] == False:
            multi_solver(graph,edge[1],des,psf,wsf+edge[2],visited,threshold)
    visited[src] = False


# def get_connected_components(graph, number_of_vertices):
#     global components
#     visited = [False for i in range(number_of_vertices)]
#     for i in range(number_of_vertices):
#         component = ""
#         if visited[i] == False:
            
# def draw_tree(graph,vertex,visited,csf):
#     visited[vertex] = True
#     for edge in graph[vertex]:
        
def bfs(graph,queue,visited,psf,origin):
    #my_map = {}
    #flag = True
    while queue:
        removed_node = queue.popleft()
        #print("level of ",removed_node," is",removed_node[2])
        #print(removed_node,"removed node",end=" ")
        visited.add(removed_node[0])
        psf = (removed_node[1]+str(removed_node[0]))
        #level = removed_node[2]
        #src = removed_node[0]
        #if flag == True:
        #my_map[origin] = [src+1]
        #flag = False
        #if level not in my_map:
        #if src != origin:
        #my_map[level] = [src]
        #else:
            #if src != origin:
                #updated_value = my_map[level]+[src]
                #my_map[level] = updated_value
        print(psf)
        #next_level = level+1
        for nbr in graph[removed_node[0]]:
            if nbr[1] not in visited:
                queue.append([nbr[1],psf])
                visited.add(nbr[1])
    #print(my_map)
         
        
        


def main():
    #global min_weight
    #global min_weight_path
    #global max_weight
    #global max_weight_path
    number_of_vertices = 8
    graph = build_graph(number_of_vertices)
    #print(graph)
    #print_graph(graph)
    #visited = [False for i in range(number_of_vertices)]
    #print(has_path(graph,0,3,visited))
    #print_all_path(graph,0,6,"",visited)
    #multi_solver(graph,0,6,"",0,visited,45)
    #print(min_weight,min_weight_path)
    #print(max_weight,max_weight_path)

    #print("threshold ceil path",threshold_ceil_path)
    #print("threshold ceil weight",threshold_ceil)
    #print("threshold floor path",threshold_floor_path)
    #print("threshold floor weight",threshold_floor)

    # for vertex in range(number_of_vertices):
    #     global components
    #     if visited[vertex] == False:
    #         csf = ""
    #         visited[vertex] = True
    #         draw_tree(graph,vertex,visited,csf)
    #         components.append(csf)

    queue = deque()
    visited = set()
    start = 0
    psf = ""
    queue.append([start,""])
    bfs(graph,queue,visited,psf,start)



main()





