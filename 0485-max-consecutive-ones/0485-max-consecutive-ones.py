class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount: int = 0
        count: int = 0

        for ele in nums:
            if ele == 1:
                count += 1
            else: count = 0
            maxCount = max(maxCount, count)

        return maxCount