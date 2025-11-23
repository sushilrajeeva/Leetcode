class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float("-inf"), float("-inf")]

        for num in nums:
            new_dp = dp[:]
            for r in range(3):
                new_r = (r + num) % 3
                new_dp[new_r] = max(new_dp[new_r], dp[r] + num)

            dp = new_dp
        return dp[0]       