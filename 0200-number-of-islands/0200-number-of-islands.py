class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        visited = [[False]* m for _ in range(n)]

        count = 0

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] == "0":
                return 
            visited[i][j] = True
            
            dfs(i-1, j) # up
            dfs(i+1, j) # down
            dfs(i, j-1) # left
            dfs(i, j+1) # right
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
        