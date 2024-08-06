class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = [[False] * m for _ in range(n)]

        def dfs(row: int, col: int):
            if board[row][col] == "O" and not visited[row][col]:
                visited[row][col] = True
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if (0 <= newRow < n) and (0 <= newCol < m) and not visited[newRow][newCol] and board[newRow][newCol] == "O":
                        dfs(newRow, newCol)
            else: return
        
        # travel top right and bottom right boundry
        for c in range(m):
            if board[0][c] == "O":
                dfs(0, c)

            if board[n-1][c] == "O":
                dfs(n-1, c)

        
        # travel left down and right down boundry
        for r in range(n):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][m-1] == "O":
                dfs(r, m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

        return board

    

        
        

        
        