from typing import *
import heapq

class MedianFinder:

    def __init__(self):
        # two heaps, large, small and large is the minHeap and small is the maxHeap
        # heaps should be equal in size approximately
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every element in small <= large
        if self.small and self.large and - 1 * self.small[0] > self.large[0]:
            val: int = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large) + 1:
            val: int = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val: int = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((self.small[0] * -1) + self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()