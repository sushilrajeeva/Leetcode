from typing import *
from collections import *

class Solution:

    def isValidMove(self, grid: List[List[int]], visited: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and not visited[row][col]

    def bfs(self, grid: List[List[int]], dist_sum: List[List[int]], reach_count: List[List[int]], row: int, col: int) -> None:
        queue = deque([(row, col, 0)])
        m: int = len(grid)
        n: int = len(grid[0])
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if self.isValidMove(grid, visited, new_row, new_col):
                    visited[new_row][new_col] = True
                    dist_sum[new_row][new_col] += d + 1
                    reach_count[new_row][new_col] += 1

                    queue.append((new_row, new_col, d + 1))


    def shortestDistance(self, grid: List[List[int]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])

        
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist_sum = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]
        total_buildings = 0

        for row in range(m):
            for col in range(n):
    
                if grid[row][col] == 1:
                    total_buildings += 1
                    self.bfs(grid, dist_sum, reach_count, row, col)
                    

        best = float("inf")
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and reach_count[r][c] == total_buildings:
                    best = min(best, dist_sum[r][c])


        return best if best != float('inf') else -1