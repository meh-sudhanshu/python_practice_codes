
def expandNode(matrix,i,j,visited,n):

    if i<0 or i>=n or j < 0 or j>=n or matrix[i][j] == 0 or visited[i][j] == 1:
        return

    visited[i][j] = 1
    expandNode(matrix,i+1,j,visited,n)
    expandNode(matrix,i-1,j,visited,n)
    expandNode(matrix,i,j+1,visited,n)
    expandNode(matrix,i,j-1,visited,n)
 



def getNumberOfIsland(matrix,n):
    visited = [[0 for i in range(n)] for j in range(n)]

    ans = 0
    # 1- land, 0- water
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                expandNode(matrix,i,j,visited,n)
                ans+=1

    return ans







def main():
    matrix = [[1,1,1,1,0,0],[0,0,0,1,1,1],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,0,1,1,1,0],
              [0,0,1,1,1,0]
              ]
    n = len(matrix)
    ans = getNumberOfIsland(matrix,n)
    print(ans)

main()