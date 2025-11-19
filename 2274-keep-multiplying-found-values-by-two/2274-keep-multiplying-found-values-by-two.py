class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet = set(nums)
        x = original
        while x in nums:
            x = x*2
        return x
        