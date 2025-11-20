class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        low = 0
        high = len(self.calendar) - 1

        if high == -1:
            self.calendar.append((start, end))
            return True
        
        while low <= high:
            mid = low + (high - low) //2
            mid_start, mid_end = self.calendar[mid]
            if (max(start, mid_start) < min(end, mid_end)):
                return False
            
            elif mid_start < start:
                low = mid + 1
            else:
                high = mid - 1
        
        self.calendar.insert(low, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)