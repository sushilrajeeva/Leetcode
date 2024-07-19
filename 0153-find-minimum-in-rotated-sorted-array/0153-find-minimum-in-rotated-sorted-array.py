class Solution:

    def isRotated(self, nums: List[int]) -> bool:
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



    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        if not self.isRotated(nums):
            return nums[0]

        breakIndex = self.getBreakIndex(nums)

        return nums[breakIndex]
        

        

        