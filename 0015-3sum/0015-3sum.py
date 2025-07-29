class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n: int = len(nums)
        nums.sort()
        
        for i in range(n-2):
            if nums[i] > 0:
                return res
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        low: int = i + 1
        high: int = len(nums) - 1

        while low < high:
            total = nums[i] + nums[low] + nums[high]

            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1

                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
