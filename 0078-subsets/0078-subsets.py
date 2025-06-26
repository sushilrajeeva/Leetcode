from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output: List[List[int]] = []
        n: int = len(nums)

        def backtracking(index: int, arr: List[int]) -> None:
            # Exit condition
            if index == n:
                output.append(arr[:])
                return

            # option 1 don't take
            backtracking(index + 1, arr)

            # option 2 take
            arr.append(nums[index])
            backtracking(index + 1, arr)
            arr.pop()
            return

        backtracking(0, [])
        
        return output
        
        