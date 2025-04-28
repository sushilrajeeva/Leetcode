class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1: return nums[0]

        # if array is not rotated
        if nums[0] < nums[-1]:
            return nums[0]

        # if rotated find peak

        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
                
            if nums[mid] > nums[-1]:
                left = mid + 1
            else: right = mid - 1

        return -1