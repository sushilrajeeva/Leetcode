class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows: int = len(grid)
        cols: int = len(grid[0])

        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isValid(row: int, col: int) -> None:
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row: int, col: int) -> bool:
            if not isValid(row, col) or grid[row][col] != 1:
                return 0

            grid[row][col] = -1
            
            area = 1

            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            
            return area
        
        max_area: int = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
                
        return max_area





        