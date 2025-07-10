import heapq
from typing import *
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCount: dict = defaultdict(int)
        n: int = len(nums)
        if k == len(nums):
            return nums

        for i in range(n):
            numCount[nums[i]] += 1

        heap = []
        heapq.heapify(heap)

        for key, value in numCount.items():
            heapq.heappush(heap, [value, key])

        for i in range(len(numCount)-k):
            heapq.heappop(heap)

        return [ele[1] for ele in heap]

        



        