class Solution:

    def valid_rows(self, board: List[List[int]]) -> bool:
        rows: int = len(board)
        cols: int = len(board[0])

        for row in range(rows):
            seen = set()
            for col in range(cols):
                if board[row][col] in seen:
                    return False
                if board[row][col] != ".":
                    seen.add(board[row][col])
        return True

    def valid_cols(self, board: List[List[int]]) -> bool:
        rows: int = len(board)
        cols: int = len(board[0])

        for col in range(cols):
            seen = set()
            for row in range(rows):
                if board[row][col] in seen:
                    return False
                if board[row][col] != ".":
                    seen.add(board[row][col])
        return True

    def valid_subgrid(self, board: List[List[int]], row: int, col: int) -> bool:
        seen = set()
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
        return True

    def valid_subgrids(self, board: List[List[int]]) -> bool:
        for row in range(3):
            for col in range(3):
                if not self.valid_subgrid(board, row * 3, col * 3):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.valid_rows(board) and
            self.valid_cols(board) and
            self.valid_subgrids(board)
            )
        