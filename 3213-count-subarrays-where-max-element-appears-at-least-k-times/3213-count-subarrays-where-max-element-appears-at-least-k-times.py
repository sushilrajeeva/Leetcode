from collections import deque
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k < 1:
            return 0
        if n == 1:
            # only one subarray [0..0]
            return 1 if k == 1 else 0

        maxEle = max(nums)
        max_pos = deque()  # indices where nums[i] == maxEle
        res = 0

        for right, v in enumerate(nums):
            if v == maxEle:
                max_pos.append(right)

            # once we've seen ≥ k copies of maxEle, every subarray ending at `right`
            # that starts at index 0..threshold will contain k of them
            if len(max_pos) >= k:
                threshold = max_pos[-k]
                res += (threshold + 1)

        return res

