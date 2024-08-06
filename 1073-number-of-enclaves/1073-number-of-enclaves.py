class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        count = [0]

        def dfsMark(row: int, col: int):
            
            if grid[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                count[0] += 1

                for r, c in directions:
                    newRow, newCol = row + r, col + c

                    if (0 <= newRow < n) and (0 <= newCol < m) and not visited[newRow][newCol] and grid[newRow][newCol] == 1:
                        dfsMark(newRow, newCol)

            else: return


        # travelling x axis boundries
        for c in range(m):
            if grid[0][c] == 1 and not visited[0][c]:
                dfsMark(0, c)
            if grid[n-1][c] == 1 and not visited[n-1][c]:
                dfsMark(n-1, c)

        # travelling y axis boundries
        for r in range(n):
            if grid[r][0] == 1 and not visited[r][0]:
                dfsMark(r, 0)
            if grid[r][m-1] == 1 and not visited[r][m-1]:
                dfsMark(r, m-1)

        count[0] = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfsMark(i, j)
        
        return count[0]



        
        