class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        if n == 0:
            return 0
        maxSum = nums[0]
        path = nums[0]

        for i in range(1, n):

            path = max(nums[i], path + nums[i])
            maxSum = max(maxSum, path)

        return maxSum