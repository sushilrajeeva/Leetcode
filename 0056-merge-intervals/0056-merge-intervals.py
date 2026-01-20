class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n: int = len(intervals)
        if n <= 1:
            return intervals

        mergeList: List[List[int]] = []

        intervals.sort(key = lambda x: x[0])

        start, end = intervals[0]

        for cur_start, cur_end in intervals[1:]:
            if cur_start <= end:
                end = max(end, cur_end)
            else:
                mergeList.append([start, end])
                start, end = cur_start, cur_end
        
        # edge case of left out interval
        mergeList.append([start, end])

        return mergeList