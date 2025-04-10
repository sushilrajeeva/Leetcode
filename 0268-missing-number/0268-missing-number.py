class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0
        for i in range(len(nums) + 1):
            xor ^= i
            if i < len(nums):
                xor^= nums[i]
        return xor
        