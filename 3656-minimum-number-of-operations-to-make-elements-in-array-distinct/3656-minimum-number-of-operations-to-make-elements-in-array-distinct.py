import math
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # at most ceil(n/3) ops will empty the array
        max_ops = math.ceil(n / 3)
        
        for ops in range(max_ops + 1):
            # remove the first 3*ops elements
            suffix = nums[3*ops:]
            # if the suffix has no duplicates, we're done
            if len(suffix) == len(set(suffix)):
                return ops
        
        # in theory we never get here, since removing all is always valid
        return max_ops
