class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()

        for index, num in enumerate(nums):
            if target-num not in seen:
                seen[num] = index
            else:
                return [seen[target-num], index]
        return [-1, -1]
        