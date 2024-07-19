class Solution:

    def isRotated(self, nums: List[int], target: int) -> int:
        return nums[0] > nums[-1]

    def getBreakIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            if mid > 0 and mid < len(nums)-1 and nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
                return mid
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def getTargetIndex(self, nums: List[int], target: int, start: int, end: int) -> int:
        left = start
        right = end

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return 0
            return -1

        if self.isRotated:
            breakIndex = self.getBreakIndex(nums)
            if nums[breakIndex] == target:
                return breakIndex
            firstPart = self.getTargetIndex(nums, target, 0, breakIndex)
            if firstPart == -1:
                return self.getTargetIndex(nums, target, breakIndex, n-1)
            return firstPart
        return self.getTargetIndex(nums, target, 0, n-1)


        