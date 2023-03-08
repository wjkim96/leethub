import numpy as np
class Solution:
    def islandHelp(self, visited, grid, sr, sc, M, N):
        perimeter = 0

        if sr < 0 or sr >= M or sc < 0 or sc >= N:
                return 1
        else:
            if grid[sr][sc] == 0:
                    return 1 
        
            else:
                if visited[sr][sc]:
                    return 0
                else:
                    visited[sr][sc] = 1
                    srLst = [sr -1, sr + 1]
                    scLst = [sc -1, sc + 1]
                    for r in srLst:
                        perimeter += self.islandHelp(visited, grid, r, sc, M, N)
                    for c in scLst:
                        perimeter += self.islandHelp(visited, grid, sr, c, M, N)

                    return perimeter
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = np.zeros_like(grid)
        perimeter = 0
        sr = -1
        sc = -1
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    sr, sc = i, j
                    break
            if sr != -1 and sc != -1:
                break
        perimeter = self.islandHelp(visited, grid, sr, sc, M, N)
        return perimeter
        