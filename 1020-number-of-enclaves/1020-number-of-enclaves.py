class Solution:
    def help(self, ans, grid, i, j):
        if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]):
            return grid, float("-inf")
        if grid[i][j] != 1:
            grid[i][j] = "v"
            return grid, 0
        else:
            grid[i][j] = "v"
            grid, A1 = self.help(ans, grid, i-1, j)
            grid, A2 = self.help(ans, grid, i+1, j)
            grid, A3 = self.help(ans, grid, i, j-1)
            grid, A4 = self.help(ans, grid, i, j+1)
            # print(grid, A1, A2, A3, A4)
            # if A1 == float("-inf") or A2 == float("-inf") or A3 == float("-inf") or A4 == float("-inf"):
            #     return grid, float("-inf")
            ans = A1 + A2 + A3 + A4 + 1
            # print(ans)
            return grid, ans
            
    def numEnclaves(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = 0
                    grid, ans = self.help(ans, grid, i, j)
                    if ans != float("-inf"):
                        print(ans)
                        area += ans
        return area
        