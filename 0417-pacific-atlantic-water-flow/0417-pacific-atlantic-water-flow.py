class Solution:
    def help(self, heights, prev, i, j, visit):
        if i <0 or j < 0:
            visit.add("Pacific")
            return
        elif i >= len(heights) or j >= len(heights[0]):
            visit.add("Atlantic")
            return
        if heights[i][j] > prev or (i,j) in visit:
            return
        else:
            prev = heights[i][j]
            visit.add((i,j))
            self.help(heights, prev, i-1, j, visit)
            self.help(heights, prev, i+1, j, visit)
            self.help(heights, prev, i, j-1, visit)
            self.help(heights, prev, i, j+1, visit)
            return 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans =[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visit = set()
                prev = float("inf")
                self.help(heights, prev, i, j, visit)
                if "Pacific" in visit and "Atlantic" in visit:
                    ans.append([i, j])
        return ans
        