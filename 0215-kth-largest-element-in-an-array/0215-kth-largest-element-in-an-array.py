import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = nums[:k]
        heapq.heapify(res)

        for i in range(k, len(nums)):
            if res[0] < nums[i]:
                heapq.heapreplace(res, nums[i])

        return res[0]
        