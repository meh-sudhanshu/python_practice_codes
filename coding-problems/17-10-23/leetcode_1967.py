minimum_weight = float('+inf')
ans = 0
modulo = (10**9 + 7)

def main():
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    #roads = [[1,0,10]]
    ans = countPaths(n,roads)
    print(ans)


def countPaths(n,roads):
    global ans
    graph = [[] for i in range(n)]
    visited = [False for i in range(n)]
    for road in roads:
        src1 = road[0]
        des1 = road
        src2 = road[1]
        pair = road[0:2]
        pair = pair[::-1]
        des2 = pair + [road[2]]
        graph[src1].append(des1)
        graph[src2].append(des2) 
    get_number_of_ways(graph,0,n-1,0,visited)
    return ans % modulo

def get_number_of_ways(graph,src,des,wsf,visited):
    global ans
    global minimum_weight
    global modulo
    if src == des:
        print(wsf)
        if wsf < minimum_weight:
            ans = 1
            minimum_weight = wsf
        elif wsf == minimum_weight:
            ans  = (ans+1)
    visited[src] = True
    for road in graph[src]:
        if visited[road[1]] == False:
            get_number_of_ways(graph,road[1],des,wsf+road[2],visited)
    visited[src] = False

main()