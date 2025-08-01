class Solution:

    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        reverse: bool = False
        rows: int = len(mat)
        cols: int = len(mat[0])
        # total diagonals = rows + cols - 1
        itrs = rows + cols - 1

        pos_dir = (-1, 1)
        neg_dir = (1, -1)

        res: List[int] = []

        for itr in range(itrs):
            # pick starting point and direction
            nr, nc = 0, 0
            if not reverse:
                if itr < rows:
                    nr, nc = itr, 0
                else:
                    nr, nc = rows - 1, itr - rows + 1
                dr, dc = pos_dir
                
            else:
                if itr < cols:
                    nr, nc = 0, itr
                else:
                    nr, nc = itr - cols + 1, cols - 1
                dr, dc = neg_dir

            # walk this diagonal until we leave the matrix
            while self.isValid(mat, nr, nc):
                res.append(mat[nr][nc])
                nr += dr
                nc += dc
            reverse = not reverse

        return res
            
                    

        