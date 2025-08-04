class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.ROWS: int = len(board)
        self.COLS: int = len(board[0])
        self.board = board
        self.directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.word = word

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, 0):
                    return True
        return False

    def backtrack(self, row: int, col: int, i: int) -> bool:

        if i == len(self.word):
            return True

        if (
            not self.isValid(row, col)
            or self.board[row][col] != self.word[i]
        ): return False

        original: str = self.board[row][col]
        self.board[row][col] = "#"

        # exploring all 4 neighboring directions
        for r, c in self.directions:
            # sudden-death return, no cleanup.
            if self.backtrack(row + r, col + c, i + 1):
                return True

        # reverting the marking
        self.board[row][col] = original

        # Tried all directions, and did not find the match
        return False


    def isValid(self, r: int, c: int) -> bool:
        return 0 <= r < self.ROWS and 0 <= c < self.COLS

        