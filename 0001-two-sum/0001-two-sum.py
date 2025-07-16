from typing import *
from collections import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        res = [-1, -1]

        for index, num in enumerate(nums):
            if not (target-num) in seen:
                seen[num] = index
            else:
                res[0] = seen[(target-num)]
                res[1] = index
                return res

        return res

            
            
        