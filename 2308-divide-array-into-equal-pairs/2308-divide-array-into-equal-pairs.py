from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq: dict = Counter(nums)
        for count in freq.values():
            if count %2 != 0: return False
        return True
        
        