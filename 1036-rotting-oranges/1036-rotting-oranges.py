from queue import Queue
from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        q: Queue = Queue()
        n = len(grid)
        m = len(grid[0])

        maxTime = 0

        visited: List[List[int]] = [[False] * m for _ in range(n)]


        freshCount = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    freshCount += 1

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while not q.empty():
            row, col, time = q.get()

            maxTime = max(maxTime, time)

            for dr, dc in directions:
                newRow, newCol = row+dr, col+dc
                if 0 <= newRow < n and 0 <= newCol < m and not visited[newRow][newCol] and grid[newRow][newCol] == 1:
                    visited[newRow][newCol] = True
                    freshCount -= 1
                    q.put((newRow, newCol, time+1))

        if freshCount > 0:
            return -1   

        return maxTime

        
                


        




        