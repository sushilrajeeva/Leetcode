from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # If the mid element is greater than the right element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is less than the right element, the minimum is in the left half
            elif nums[mid] < nums[right]:
                right = mid
            # If the mid element is equal to the right element, we can't determine the minimum part, so reduce the search space
            else:
                right -= 1
        
        return nums[left]