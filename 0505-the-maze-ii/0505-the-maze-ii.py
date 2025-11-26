from typing import List
from heapq import heappush, heappop
import math

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        sr, sc = start
        dr, dc = destination
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # dist[r][c] = shortest distance found so far to stop at (r, c)
        dist = [[math.inf] * n for _ in range(m)]
        dist[sr][sc] = 0
        
        # Min-heap of (distance_so_far, row, col)
        heap = []
        heappush(heap, (0, sr, sc))
        
        while heap:
            d, r, c = heappop(heap)
            
            # If this popped state is worse than what we know, skip it
            if d > dist[r][c]:
                continue
            
            # If we've reached destination with the minimal distance
            if [r, c] == destination:
                return d
            
            # Try rolling in all 4 directions
            for drc, dcc in directions:
                nr, nc = r, c
                steps = 0
                
                # Roll until hit a wall or boundary
                while (0 <= nr + drc < m and
                       0 <= nc + dcc < n and
                       maze[nr + drc][nc + dcc] == 0):
                    nr += drc
                    nc += dcc
                    steps += 1
                
                new_dist = d + steps
                # If this path to (nr, nc) is shorter, update and push
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heappush(heap, (new_dist, nr, nc))
        
        # Destination unreachable
        return -1
