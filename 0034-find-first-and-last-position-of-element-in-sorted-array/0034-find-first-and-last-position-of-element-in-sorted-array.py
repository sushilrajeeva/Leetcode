class Solution:

    def lowerBound(self, nums: List[int], target: int) -> int:

        n: int = len(nums)
        left: int = 0
        right: int = n-1

        while left<=right:
            mid: int = left + (right - left)//2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if left >= n or nums[left] != target:
            return -1

        return left

    def upperBound(self, nums: List[int], target: int) -> int:
        
        n: int = len(nums)
        left: int = 0
        right: int = n-1

        while left<=right:
            mid: int = left + (right-left)//2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right if nums[right] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        leftIndex: int = self.lowerBound(nums, target)
        if leftIndex == -1:
            return [-1, -1]
        rightIndex: int = self.upperBound(nums, target)

        return [leftIndex, rightIndex]
        