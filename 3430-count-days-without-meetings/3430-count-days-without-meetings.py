class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort(key=lambda x: x[0])
        
        # Step 2: Merge overlapping meetings
        merged_meetings = []
        current_meeting = meetings[0]
        for meeting in meetings[1:]:
            # If the current meeting overlaps with the next, merge them.
            if meeting[0] <= current_meeting[1]:
                current_meeting[1] = max(current_meeting[1], meeting[1])
            else:
                merged_meetings.append(current_meeting)
                current_meeting = meeting
        merged_meetings.append(current_meeting)


        def markUnavailable(start: int, end: int) -> None:
            return (end - start + 1)
        
        total_days_unavailable: int = 0
        for meeting in merged_meetings:
            total_days_unavailable += markUnavailable(meeting[0], meeting[1])
        
        return max(days - total_days_unavailable, 0)
        