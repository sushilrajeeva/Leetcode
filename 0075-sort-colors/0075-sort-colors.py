class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def parity_sort(nums: List[int], i: int, key: int) -> int:
            left: int = i
            right: int = len(nums) - 1

            while left < right:
                if nums[left] == key:
                    left += 1
                elif nums[right] != key:
                    right -= 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
            return left

        next_index = parity_sort(nums, 0, 0)
        next_index = parity_sort(nums, next_index, 1)

        

        
        

        