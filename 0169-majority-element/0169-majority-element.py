class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        ele = None
        count = 0

        # moore's voting algorithm
        

        for num in nums:
            if count == 0:
                ele = num
                count = 1
            else:
                if ele == num:
                    count += 1
                else:
                    count -= 1
        return ele
        
