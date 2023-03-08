class Solution:
    
    def checkAndColor(self, image, sr, sc, prev, M, N, color):
        if sr < 0 or sr >= M or sc < 0 or sc >= N:
            return image
        else:
            if image[sr][sc] != color and image[sr][sc] == prev:
                image[sr][sc] = color
                srLst = [sr - 1, sr + 1]
                scLst = [sc - 1, sc + 1]
                for r in srLst:
                    image = self.checkAndColor(image, r, sc, prev, M, N, color)
                for c in scLst:
                    image = self.checkAndColor(image, sr, c, prev, M, N, color)
                return image
            else:
                return image
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M = len(image)
        N = len(image[0])

        prev = image[sr][sc]
        image = self.checkAndColor(image, sr, sc, prev, M, N, color)
        return image
        