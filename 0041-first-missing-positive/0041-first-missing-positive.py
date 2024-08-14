class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n: int = len(nums)
        containsOne: bool = False
        for i in range(n):
            if nums[i] == 1: containsOne = True
            elif nums[i] <= 0 or nums[i] > n: nums[i] = 1
        
        if not containsOne: return 1

        for i in range(n):
            key: int = abs(nums[i])-1
            if nums[key] > 0: nums[key] *= -1
        
        for i in range(n):
            if nums[i] > 0: return i+1

        return n+1

        


        