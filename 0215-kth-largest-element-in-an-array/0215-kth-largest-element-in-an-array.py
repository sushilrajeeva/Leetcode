import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        n = len(nums)
        x = n - k + 1
        
        val = 0
        
        while x > 0:
            val = heapq.heappop(nums)
            x -= 1
            
        return val
            
    
        