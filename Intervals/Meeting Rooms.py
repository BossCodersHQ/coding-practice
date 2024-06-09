from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        earliest = 0
        for interval in intervals:
            if interval[0] < earliest:
                return False
            earliest = max(earliest, interval[1])
        return True
