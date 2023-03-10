class Solution:
    def checkArea(self, area, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        else:
            grid[i][j] = "v"
            A1 = self.checkArea(area, grid, i-1, j)
            A2 = self.checkArea(area, grid, i+1, j)
            A3 = self.checkArea(area, grid, i, j-1)
            A4 = self.checkArea(area, grid, i, j+1)
            area = area + A1 + A2 + A3 + A4
            # print(i, j, area)
            area += 1
            return area 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.checkArea(0, grid, i, j)
                    if area > ans:
                        ans = area
        return ans
        