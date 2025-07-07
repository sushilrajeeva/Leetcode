
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev_start = -1
        prev_end = -1

        for x, y in intervals:
            if prev_end > x:
                return False
            prev_start = x
            prev_end = y

        return True
        