class Solution:
    def help(self, grid, i, j, graph):
        if i < 0 or i >= len(grid) or j<0 or j >= len(grid[0]) or grid[i][j] == 'v':
            return 
        if grid[i][j] == 0:
            grid[i][j] = 'v'
            return 
        else:
            graph.add((i,j))
            grid[i][j] = 'v'
            self.help(grid, i-1, j, graph)
            self.help(grid, i+1, j, graph)
            self.help(grid, i, j-1, graph)
            self.help(grid, i, j+1, graph)
            return 
    
            
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    graph2 = set()
                    self.help(grid2, i, j, graph2)
                    if graph2:
                        same = 1
                        for g in graph2:
                            if grid1[g[0]][g[1]] == 0:
                                same = 0
                                break
                        if same:
                            ans += 1
        return ans
                                
                                
        