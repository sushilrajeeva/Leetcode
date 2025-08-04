class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return matrix

        res: List[int] = []

        rows: int = len(matrix)
        cols: int = len(matrix[0])

        top: int = 0
        bottom: int = rows - 1

        left: int = 0
        right: int = cols - 1

        while top <= bottom and left <= right:
            
            # 1) Traverse from left → right along the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1 # moving down the boundry

            # 2) Traverse from top → bottom along the right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1 # moving left of the right boundry

            # 3) If there’s still a bottom row, traverse right → left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4) If there’s still a left column, traverse bottom → top (if it still exist)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res

            