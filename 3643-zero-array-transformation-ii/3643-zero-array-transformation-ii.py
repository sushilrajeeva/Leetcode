from typing import List

class Solution:

    def canTransform(self, nums: List[int], queries: List[int], right: int) -> bool:
        n: int = len(nums)
        total: int = 0

        diff: List[int] = [0] * (n+1)

        for i in range(right):
            l: int = queries[i][0]
            r: int = queries[i][1]
            val: int = queries[i][2]

            diff[l] += val
            diff[r+1] -= val

        for i in range(n):
            total += diff[i]
            if total < nums[i]: return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n: int = len(nums)
        m: int = len(queries)
        left: int = 0
        right: int = m

        if not self.canTransform(nums, queries, right): return -1

        while left <= right:
            mid: int = int(left + (right - left)//2)
            if self.canTransform(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
       
