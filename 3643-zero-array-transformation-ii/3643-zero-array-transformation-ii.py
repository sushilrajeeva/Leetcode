from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        # Helper function to check if the first k queries are sufficient.
        # We use a difference array to quickly calculate the total available decrement
        # for each index.
        def can_zero(k: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            
            current = 0
            for i in range(n):
                current += diff[i]
                # If the total available decrement at index i is less than the value of nums[i],
                # then it's not possible to zero out this index.
                if current < nums[i]:
                    return False
            return True
        
        # Binary search for the minimum k that can zero out the array.
        lo, hi = 0, m + 1  # hi is set to m+1 so that if no k in [0, m] works, we detect it.
        res = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_zero(mid):
                res = mid
                hi = mid  # try to find a smaller k
            else:
                lo = mid + 1
        
        return res
