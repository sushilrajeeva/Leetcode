class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        visited = [[False] * m for _ in range(n)]
        key = image[sr][sc]

        def dfs(sr: int, sc: int):
            if sr < 0 or sr >= n or sc < 0 or sc >= m or image[sr][sc] != key or visited[sr][sc]:
                return
            
            visited[sr][sc] = True
            image[sr][sc] = color

            dfs(sr - 1, sc) # UP
            dfs(sr + 1, sc) # DOWN
            dfs(sr, sc - 1) # LEFT
            dfs(sr, sc + 1) # RIGHT

        
        dfs(sr, sc)

        return image