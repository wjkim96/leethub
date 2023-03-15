class Solution:           
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M = len(grid)
        V = [[0 for _ in range(M)] for __ in range(M)]
        V[0][0] = 1

        if (M == 1 & grid[0][0]) or grid[0][0]:
            return -1
            

        q = [(0,0)]
        while q:
            # print(q)
            i, j = q.pop(0)
            di = [1, 1, 1, 0, 0, -1, -1, -1]
            dj = [1, 0, -1, 1, -1, 1, 0, -1]

            for d in range(8):
                ni, nj = di[d] + i, dj[d] + j
                if ni < 0 or ni >= M or nj < 0 or nj >= M or V[ni][nj] or grid[ni][nj] == 1:
                    continue
                else:
                    V[ni][nj] = V[i][j] + 1
                    q.append((ni, nj))

        
        if not V[M-1][M-1]:
            return -1
        return V[M-1][M-1]
