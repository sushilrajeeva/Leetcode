class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = abs(nums[0] - nums[len(nums)-1])
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, abs(nums[i] - nums[i-1]))

        return maxDiff