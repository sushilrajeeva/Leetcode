class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        n: int = len(nums)
        l: int = 0
        r: int = n -1

        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 == 1:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return nums
        