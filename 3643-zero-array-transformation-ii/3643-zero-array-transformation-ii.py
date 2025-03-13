from typing import List

class Solution:
    def canTransform(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        total = 0
        diff = [0] * (n + 1)

        # Process the first k queries to build the difference array
        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            if r + 1 < len(diff):
                diff[r + 1] -= val

        # Check if each element can be reduced to zero
        for i in range(n):
            total += diff[i]
            if total < nums[i]:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        m = len(queries)
        left = 0
        right = m

        # If even all queries can't transform the array, return -1
        if not self.canTransform(nums, queries, right):
            return -1

        # Binary search for the minimum number of queries needed
        while left <= right:
            mid = (left + right) // 2
            if self.canTransform(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
