import java.util.Arrays;

public class TicTacToe {
    private final int n;
    private final int[] rows;
    private final int[] cols;
    private int diagonal;
    private int antiDiagonal;
    private final int[][] board;

    public TicTacToe(int n) {
        this.n = n;
        this.rows = new int[n];
        this.cols = new int[n];
        this.diagonal = 0;
        this.antiDiagonal = 0;
        this.board = new int[n][n];          // all zeroes by default
    }

    private boolean isValid(int row, int col) {
        return row >= 0 && row < n && col >= 0 && col < n;
    }

    /**
     * Player {1, 2} makes a move at (row, col).
     * @return   0 = no one won yet, 1 = player 1 wins, 2 = player 2 wins, -1 = invalid move
     */
    public int move(int row, int col, int player) {
        // out of bounds or cell already taken
        if (!isValid(row, col) || board[row][col] != 0) {
            return -1;
        }

        // mark the board
        board[row][col] = player;

        // convert player to +1 / -1
        int toAdd = (player == 1 ? +1 : -1);

        // update row/col counters
        rows[row] += toAdd;
        cols[col] += toAdd;

        // update diagonals if applicable
        if (row == col) {
            diagonal += toAdd;
        }
        if (col == (n - row - 1)) {
            antiDiagonal += toAdd;
        }

        // check if this move causes a win
        if (Math.abs(rows[row]) == n
         || Math.abs(cols[col]) == n
         || Math.abs(diagonal) == n
         || Math.abs(antiDiagonal) == n) {
            return player;
        }

        // no winner yet
        return 0;
    }
}
