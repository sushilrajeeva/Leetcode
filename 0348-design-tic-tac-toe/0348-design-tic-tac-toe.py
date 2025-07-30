class TicTacToe:

    def __init__(self, n: int):
        self.rows: List[int] = [0] * n
        self.cols: List[int] = [0] * n
        self.diagonal: int = 0
        self.antiDiagonal: int = 0
        self.n = n
        self.board: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]

    def isValidMove(self, row: int, col: int) -> bool:
        if not (0 <= row < self.n and 0 <= col < self.n):
            raise IndexError("Move out of bounds!")
        if self.board[row][col] != 0:
            raise ValueError(f"Cell ({row}, {col}) is already taken")

    def move(self, row: int, col: int, player: int) -> int:

        self.isValidMove(row, col)

        self.board[row][col] = player

        currentPlayer: int = 1 if player == 1 else -1
        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer

        if row == col:
            self.diagonal += currentPlayer
        
        if col == (len(self.cols) - row - 1):
            self.antiDiagonal += currentPlayer

        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.antiDiagonal) == self.n):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)