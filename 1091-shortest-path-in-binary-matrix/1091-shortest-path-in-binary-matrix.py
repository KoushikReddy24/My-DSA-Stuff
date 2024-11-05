class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        L = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        n,m = len(grid),len(grid[0])

        if grid[0][0] == 1 or grid[n-1][m-1]==1:
            return -1

        visited = [[0]*m for _ in range(n)]
        d = [[float('inf')]*m for _ in range(n)]
        def valid(i,j):
            if i < 0 or i > n-1 or j < 0 or j > m-1 or grid[i][j] == 1:
                return False
            return True
        
        q = []
        q.append([0,0])
        d[0][0] = 0
        visited[0][0] = 1
        while q:
            i,j = q.pop(0)

            for di,dj in L:
                x = i + di
                y = j + dj

                if valid(x,y) and d[x][y] > d[i][j] + 1 and not visited[x][y]:
                    d[x][y] = d[i][j] + 1
                    q.append([x,y])
        
        if d[n-1][m-1] == float('inf'):
            return -1
        return d[n-1][m-1] + 1

