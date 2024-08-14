import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCount: dict = dict()
        n: int = len(nums)

        for i in range(n):
            numCount[nums[i]] = numCount.get(nums[i], 0) + 1

        heap = []
        heapq.heapify(heap)

        for key, value in numCount.items():
            heapq.heappush(heap, [value, key])

        for i in range(len(numCount)-k):
            heapq.heappop(heap)

        return [ele[1] for ele in heap]

        



        