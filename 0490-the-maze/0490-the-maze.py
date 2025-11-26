from collections import deque
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Visited cells where the ball can *stop*
        visited = [[False] * n for _ in range(m)]
        
        q = deque()
        q.append((start[0], start[1]))
        visited[start[0]][start[1]] = True
        
        while q:
            r, c = q.popleft()
            
            # If we can stop at destination, return True
            if [r, c] == destination:
                return True
            
            # Try all 4 directions
            for dr, dc in directions:
                nr, nc = r, c
                
                # Roll until we hit a wall or boundary
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                
                # (nr, nc) is the stopping position in this direction
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        # If BFS finishes without reaching destination
        return False
