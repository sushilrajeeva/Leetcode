from collections import *
class Solution:

    def isValidMove(self, grid: List[List[int]], row, col) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions: List[Tuple[int, int]] = [(1,0),(0,1),(-1,0),(0,-1)]
        max_time: int = 0
        m: int = len(grid)
        n: int = len(grid[0])
        queue = deque([])
        fresh_count: int = 0

        # create a queue of rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1

        while len(queue) > 0:
            row, col, time = queue.popleft()
            max_time = max(max_time, time)

            for _row, _col in directions:
                r = row + _row
                c = col + _col
                if self.isValidMove(grid, r, c):
                    queue.append((r, c, time + 1))
                    grid[r][c] = 2
                    fresh_count -= 1
        
        if fresh_count > 0:
            return -1
        
        return max_time



        