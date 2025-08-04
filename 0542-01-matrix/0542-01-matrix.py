from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        m = len(mat)
        n = len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        queue = deque()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    dist[row][col] = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            
            for r, c in directions:
                nr, nc = row + r, col + c
                if valid(nr, nc) and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[row][col] + 1
                    queue.append((nr, nc))
                    
        
        return dist