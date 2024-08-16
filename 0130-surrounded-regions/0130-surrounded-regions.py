class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < m

        def dfs(row: int, col: int):
            if not isValid(row, col) or board[row][col] != "O":
                return

            board[row][col] = "-O"

            for direction in directions:
                newRow, newCol = direction[0] + row, direction[1] + col
                dfs(newRow, newCol)
        
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
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "-O":
                    board[i][j] = "O"

        return board

    

        
        

        
        