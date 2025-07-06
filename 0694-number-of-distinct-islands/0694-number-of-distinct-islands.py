class Solution:

    def is_valid_move(self,row: int, col: int, grid: List[List[int]], visited: List[List[bool]]) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not visited[row][col] and grid[row][col] == 1

    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])

        visited: List[List[bool]] = [[False] * n for _ in range(m)]
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        unique_islands: Set[Tuple[Tuple[int, int]]] = set()

        def dfs(row: int, col: int, base_row: int, base_col: int, track: List[Tuple[int, int]]) -> None:
            if not self.is_valid_move(row, col, grid, visited):
                return
            visited[row][col] = True
            track.append((row - base_row, col - base_col))

            for direction in directions:
                new_row: int = row + direction[0]
                new_col: int = col + direction[1]

                dfs(new_row, new_col, base_row, base_col, track)
            
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == 1:
                    track: List[Tuple[int, int]] = []
                    dfs(r, c, r, c, track)
                    shape: Tuple[Tuple[int, int]] = tuple(sorted(track))
                    unique_islands.add(shape)
        return len(unique_islands)




        