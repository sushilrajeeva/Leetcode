import heapq
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        maxLen = 0

        left = 0
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1

            maxLen = max(maxLen, right - left + 1) 

        return n - maxLen

        