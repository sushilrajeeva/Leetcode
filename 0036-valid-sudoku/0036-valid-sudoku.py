class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize a set to keep track of seen numbers
        seen = set()

        # Iterate through each cell in the 9x9 Sudoku board
        for row in range(9):
            for col in range(9):
                number = board[row][col]

                # Check only the cells that are filled with a number
                if number != ".":

                    # Create unique identifiers for the row, column, and box
                    row_key = f"{number} in row {row}"
                    col_key = f"{number} in column {col}"
                    box_key = f"{number} in box {row//3}-{col//3}"

                    # Check if any of these identifiers already exist in 'seen'
                    if (row_key in seen) or (col_key in seen) or (box_key in seen):
                        # If any identifier is already seen, the board is invalid
                        return False
                    
                    # Add the new identifiers to the 'seen' set
                    seen.update({row_key, col_key, box_key})

        # If no duplicates are found, the board is valid
        return True
