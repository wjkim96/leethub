class Solution:
    def help(self, direction, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            direction.discard(1)
            return grid, direction
        if grid[i][j] != 0:
            return grid, direction
        else:
            grid[i][j] = "v"
            if self.help(direction, grid, i-1, j)[1]:
                direction.add("L")
            # else:
            #     return False
            if self.help(direction, grid, i+1, j)[1]:
                direction.add("R")
            # else:
            #     return False
            if self.help(direction, grid, i, j-1)[1]:
                direction.add("B")
            # else:
            #     return False
            if self.help(direction, grid, i, j+1)[1]:
                direction.add("T")
            # else:
            #     return False
            return grid, direction
                
            
            
            
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    direction = {1}
                    grid, direction = self.help(direction, grid, i, j)
                    if direction and len(direction) == 5:
                        ans += 1
        return ans