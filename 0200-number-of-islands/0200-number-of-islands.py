class Solution:

    def isValidMove(self, grid: List[List[int]], row: int, col: int, visited: List[List[int]]) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not visited[row][col] and grid[row][col] == "1"

    def dfs(self, row: int, col: int, grid: List[List[str]], visited: List[List[bool]], directions: List[Tuple[int, int]]) -> None:

        if not self.isValidMove(grid, row, col, visited):
            return

        visited[row][col] = True

        for direction in directions:
            new_row: int = row + direction[0]
            new_col: int = col + direction[1]
            self.dfs(new_row, new_col, grid, visited, directions)

    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0
        m: int = len(grid)
        n: int = len(grid[0])
        visited: List[List[bool]] = [[False] * n for _ in range(m)]
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        

        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == "1":
                    count += 1
                    self.dfs(r, c, grid, visited, directions)
                    

        return count

        


        