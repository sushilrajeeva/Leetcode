import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            stone1 = (heapq.heappop(maxHeap)) * -1
            stone2 = (heapq.heappop(maxHeap)) * -1

            newStone = stone1 - stone2
            if newStone > 0:
                heapq.heappush(maxHeap, -newStone)
        
        return 0 if not maxHeap else -maxHeap[0]

        