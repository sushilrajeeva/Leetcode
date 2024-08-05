from queue import Queue
from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        q: Queue = Queue()
        n = len(grid)
        m = len(grid[0])

        maxTime = [0]

        visited: List[List[int]] = [[False] * m for _ in range(n)]


        freshCount = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    freshCount += 1


        while not q.empty():
            row, col, time = q.get()

            maxTime[0] = max(maxTime[0], time)

            if (0 <= row - 1 < n) and (0 <= col < m) and (not visited[row-1][col]) and grid[row-1][col] == 1: # UP
                q.put((row-1, col, time + 1))
                freshCount -= 1
                visited[row-1][col] = True

            if (0 <= row + 1 < n) and (0 <= col < m) and (not visited[row+1][col]) and grid[row+1][col] == 1: # DOWN
                q.put((row+1, col, time + 1))
                freshCount -= 1
                visited[row+1][col] = True

            if (0 <= row < n) and (0 <= col - 1 < m) and (not visited[row][col-1]) and grid[row][col-1] == 1: # LEFT
                q.put((row, col-1, time + 1))
                freshCount -= 1
                visited[row][col-1] = True

            if (0 <= row < n) and (0 <= col + 1 < m) and (not visited[row][col+1]) and grid[row][col+1] == 1: # RIGHT
                q.put((row, col+1, time + 1))
                freshCount -= 1
                visited[row][col+1] = True

        if freshCount > 0:
            return -1   

        return maxTime[0]

        
                


        




        