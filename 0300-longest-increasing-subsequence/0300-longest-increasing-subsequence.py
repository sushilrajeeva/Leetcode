class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        length = 0

        memo = [[-1] * n for _ in range(n+1)]

        def dp(index, prev):
            if index == n:
                return 0

            if memo[index][prev+1] != -1: return memo[index][prev+1]

            # don't take
            length = 0 + dp(index + 1, prev)

            # take
            if prev == -1 or nums[index] > nums[prev]:
                length = max(length, 1 + dp(index+1, index))
            memo[index][prev+1] = length
            return memo[index][prev+1]

        return dp(0, -1)


        