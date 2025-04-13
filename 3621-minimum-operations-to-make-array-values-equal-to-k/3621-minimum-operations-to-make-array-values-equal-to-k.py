class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        attempts: int = 0

        seen = set()
        n = len(nums)


        for value in nums:
            if value < k: return -1
            elif value > k: seen.add(value)

        return len(seen)

        

        
        

        