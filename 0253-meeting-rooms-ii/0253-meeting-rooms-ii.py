from typing import *
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        heap = []
        heapq.heappush(heap, intervals[0][1]) # push the end time of the first interval

        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
        
        