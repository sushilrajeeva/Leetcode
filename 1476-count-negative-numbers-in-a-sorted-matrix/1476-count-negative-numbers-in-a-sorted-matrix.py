class Solution:

    def getNegativesCount(self, row: List[int]) -> int:

        n = len(row)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right-left)//2

            if row[mid] >= 0:
                left = mid + 1
            else:
                right = mid - 1

        if left >= n:
            return 0
        return n-left

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            count += self.getNegativesCount(row)

        return count