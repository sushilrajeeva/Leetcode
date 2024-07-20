class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        

        n = len(nums)
        left = 0
        right = n-1

        if n == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[right] != nums[right-1]: # comparing the last with second last
            return nums[right]

        while left<=right:
            mid = left + (right-left)//2

            # Check if the mid element is the single element
            if mid > 0 and mid < n - 1 and nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            # Check if the mid element is the start of a pair
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]
        