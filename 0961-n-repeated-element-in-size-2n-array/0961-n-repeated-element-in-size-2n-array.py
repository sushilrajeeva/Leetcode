class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for k in (1, 2, 3):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
