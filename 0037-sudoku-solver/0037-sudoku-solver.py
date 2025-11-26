from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # sets to track used digits in rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # initialize sets and list of empty positions
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    box_id = (r // 3) * 3 + (c // 3)
                    boxes[box_id].add(ch)

        def backtrack(idx: int) -> bool:
            # all empty cells filled
            if idx == len(empties):
                return True

            r, c = empties[idx]
            box_id = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch in rows[r] or ch in cols[c] or ch in boxes[box_id]:
                    continue

                # place ch
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_id].add(ch)

                if backtrack(idx + 1):
                    return True

                # undo
                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box_id].remove(ch)

            return False

        backtrack(0)
