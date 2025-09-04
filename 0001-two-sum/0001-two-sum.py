class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()
        for index, num in enumerate(nums):
            if num in complement:
                return [complement[num], index]
            else:
                complement[target-num] = index
        return [-1, -1]
        