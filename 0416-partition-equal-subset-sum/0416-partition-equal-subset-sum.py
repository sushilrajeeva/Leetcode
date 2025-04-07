class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n: int = len(nums)
        res: List[bool] = [False]
        total: int = sum(nums)
        target: int = total // 2

        if total%2 != 0: return False

        memo = {}

        def dp(i, current_sum):

            if res[0]: return

            if current_sum == target:
                res[0] = True
                return
            
            if i == n or current_sum > target: return

            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            # don't take
            no = dp(i+1, current_sum)

            # take
            yes = dp(i+1, current_sum + nums[i])
            memo[(i, current_sum)] = yes or no
            return memo[(i, current_sum)]


        dp(0, 0)

        return res[0]