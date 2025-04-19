class Solution:

    def lowerBound(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        result: int = 0

        while left <= right:
            total = nums[left] + nums[right]

            if total < target:
                result += right - left
                left += 1
            else:
                right -= 1

        return result

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lowerBound(nums, upper + 1) - self.lowerBound(nums, lower)

