class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1: return nums

        results = [0] * n

        for i in range(n):
            x = i
            if nums[i] > 0:
                x = (i+nums[i]) % n
            elif nums[i] < 0:
                x = (i-abs(nums[i])) % n
            else:
                x = i
            results[i] = nums[x]

        return results



        