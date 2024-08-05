class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        
        return False
        