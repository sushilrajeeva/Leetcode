class Solution:

    def is_valid_move(self,row: int, col: int, grid: List[List[int]], visited: List[List[bool]]) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not visited[row][col] and grid[row][col] == 1

    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])

        visited: List[List[bool]] = [[False] * n for _ in range(m)]
        directions: List[Tuple[int,int,str]] = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

        unique_islands: Set[Tuple[str, ...]] = set()

        def dfs(row: int, col: int, signature: List[str], origin_marker) -> None:
            if not self.is_valid_move(row, col, grid, visited):
                return
            visited[row][col] = True
            signature.append(origin_marker)

            for direction in directions:
                new_row: int = row + direction[0]
                new_col: int = col + direction[1]
                mark: str = direction[2]

                dfs(new_row, new_col, signature, mark)
            
            signature.append("O")
            
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == 1:
                    signature: List[str] = []
                    dfs(r, c, signature, "S")
                    unique_islands.add(tuple(signature))
        return len(unique_islands)




        