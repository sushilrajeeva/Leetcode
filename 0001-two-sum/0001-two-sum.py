class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            key = target - num
            if key in seen:
                return [seen[key], index]
            else:
                seen[num] = index
                
        return [-1, -1]
                
        