class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        di = [1,0,0,-1]
        dj = [0,1,-1,0]
        
        M = len(mat)
        N = len(mat[0])
        
        q= []
        
        for i in range(M):
            for j in range(N):
                if not mat[i][j]: q.append((i,j))
                    
        V = [[0 for _ in range(N)] for __ in range(M)]
        
        while q:
            i, j = q.pop(0)
            
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                
                if ni < 0 or ni >= M or nj < 0 or nj >= N or V[ni][nj] or mat[ni][nj] == 0:
                    continue
                else:
                    V[ni][nj] = V[i][j] + 1
                    q.append((ni,nj))
                    
        return V
                
                
            
            
        
        
        