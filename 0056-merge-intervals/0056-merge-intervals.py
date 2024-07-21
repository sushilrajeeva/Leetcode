class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        n = len(intervals)

        if n == 1:
            return intervals

        def sortFirst(interval: List[int]):
            return interval[0]

        intervals.sort(key=sortFirst)
        
        currentRange = intervals[0]

        

        for i in range(1, n):
            interval = intervals[i]
            if currentRange[1] < interval[0]:
                output.append(currentRange)
                currentRange = interval
            else:
                currentRange[1] = max(currentRange[1], interval[1])
        
        output.append(currentRange)

        return output