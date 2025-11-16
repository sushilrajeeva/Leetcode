class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        print(nums)

        x = nums[-3] * nums[-2] * nums[-1]
        y = nums[0] * nums[1] * nums[-1]

        return x if x > y else y
        