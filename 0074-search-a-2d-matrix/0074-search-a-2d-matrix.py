class Solution:

    def getTargetRow(self, matrix:[List[List[int]]], target: int) -> int:
        left, right = 0, len(matrix)-1
        while left<=right:
            mid = left + (right-left)//2
            if matrix[mid][0] == target:
                return mid
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def searchTargetRow(self, matrix: List[List[int]], target: int, row: int):
        left = 0
        right = len(matrix[0])-1

        while left<=right:
            mid = left + (right-left)//2

            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
            


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
    
        targetRow = self.getTargetRow(matrix, target)

        if targetRow < 0 or targetRow > len(matrix):
            return False

        if matrix[targetRow][0] <= target <= matrix[targetRow][len(matrix[0])-1]:
            return self.searchTargetRow(matrix, target, targetRow)

        return False
        