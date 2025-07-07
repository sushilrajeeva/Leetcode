from typing import *
from collections import *

class Solution:

    def isValidMove(self, grid: List[List[int]], distances: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and distances[row][col] == -1

    def shortestDistance(self, grid: List[List[int]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])

        
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_buildings = 0

        # Two helper grids:
        #   total_dist[i][j] = sum of distances from all buildings seen so far
        #   reach_count[i][j] = how many buildings have reached (i,j)
        total_dist = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings += 1
                    distances: List[List[int]] = [[-1] * n for _ in range(m)]
                    queue = deque([(i, j)])
                    distances[i][j] = 0

                    while queue:
                        row, col = queue.popleft()

                        for direction in directions:
                            r, c = direction
                            new_row = r + row
                            new_col = c + col
                            if self.isValidMove(grid, distances, new_row, new_col):
                                distances[new_row][new_col] = distances[row][col] + 1
                                queue.append((new_row, new_col))
                                total_dist[new_row][new_col] += distances[new_row][new_col]
                                reach_count[new_row][new_col] += 1

        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    ans = min(ans, total_dist[i][j])

        return ans if ans != float('inf') else -1


        