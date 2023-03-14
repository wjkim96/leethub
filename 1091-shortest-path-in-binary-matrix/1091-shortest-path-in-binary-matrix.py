class Solution:
    def help(self, grid, q, dist, ans, i, j):
        # q = q[:]
        if i <0 or i>= len(grid) or j <0 or j >= len(grid) or grid[i][j] == 1:
            return 
        else:
            if q[i * len(grid) + j] == 0 or q[i * len(grid) + j] > dist:
                if (i, j) == (len(grid)-1, len(grid)-1):
                    ans.append(dist)
                    return
                else:
                    q[i * len(grid) + j] = dist
                    dist += 1
                    self.help(grid, q, dist, ans, i+1, j+1)
                    self.help(grid, q, dist, ans, i+1, j)
                    self.help(grid, q, dist, ans, i, j+1)
                    self.help(grid, q, dist, ans, i-1, j+1)
                    self.help(grid, q, dist, ans, i+1, j-1)
                    self.help(grid, q, dist, ans, i-1, j)
                    self.help(grid, q, dist, ans, i, j-1)
                    self.help(grid, q, dist, ans, i-1, j-1)
                # grid[i][j] = 'v'
                return

                
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # q = [0 for _ in range(len(grid) **2)]
        # ans = []
        # self.help(grid, q, 1, ans, 0, 0)
        # # print(ans)
        # if ans:
        #     return min(ans)
        # else:
        #     return -1

        if(grid[0][0]==1): 
            return -1
        if len(grid) == 1:
            return 1
        
        dy = [1, 1, 1,  0, 0,  -1, -1, -1]
        dx = [1, 0, -1, 1, -1,  1, 0,  -1]

        n = len(grid)
        V = [[0 for _ in range(n)] for __ in range(n)] # n x n

        s = (0,0)
        q = []
        q.append(s)


        while q:
            y,x = q.pop(0)

            for d in range(8):
                ny, nx = y + dy[d], x+dx[d]
                # out of bound
                if (ny < 0) | (nx < 0) | (ny >= n) | (nx >= n):
                    continue
                # wall
                if grid[ny][nx] == 1:
                    continue
                # visit
                if V[ny][nx]:
                    continue

                V[ny][nx] = V[y][x] + 1
                q.append((ny, nx))
        
        if V[n-1][n-1] == 0:
            return -1
        return V[n-1][n-1] + 1