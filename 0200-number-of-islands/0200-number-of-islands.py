import numpy as np


class Solution:
    def numIslandsHelp(self, ans, visited, grid, sr, sc, M, N):
        # print(sr, sc)
        if sr >= M or sc >= N or sr < 0 or sc < 0:
            return visited, ans
        if visited[sr][sc]:
            return visited, ans
        else:
            if grid[sr][sc] == '0':
                visited[sr][sc] = 1
                return visited, ans
            else:
                visited[sr][sc] = 1
                self.numIslandsHelp(ans, visited, grid, sr -1, sc, M, N)
                self.numIslandsHelp(ans, visited, grid, sr +1, sc, M, N)
                self.numIslandsHelp(ans, visited, grid, sr, sc-1, M, N)
                self.numIslandsHelp(ans, visited, grid, sr, sc+1, M, N)
                ans += 1
                # print(visited, ans)
                return visited, ans 

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = np.zeros_like(grid)
        M = len(grid)
        N = len(grid[0])
        for sr in range(M):
            for sc in range(N):
                # print(sr,sc)
                visited, ans = self.numIslandsHelp(ans, visited, grid, sr, sc, M, N)
                # print(visited, ans)
                # print(grid)
        return ans
