class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n: int = len(grid)
        m: int = len(grid[0])

        def isValid(row: int, col: int) -> bool:
            if row < 0 or row >= n or col < 0 or col >= m: return False
            return True

        def dfs(row: int, col: int) -> int:
            if not isValid(row, col) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            area += dfs(row+1, col)
            area += dfs(row-1, col)
            area += dfs(row, col+1)
            area += dfs(row, col-1)

            return area

        maxArea: int = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea