from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        earliest = 0
        for interval in intervals:
            if interval[0] < earliest:
                return False
            earliest = interval[1]
        return True


if __name__ == "__main__":
    s = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert s.canAttendMeetings(intervals) == False
    intervals = [[7, 10], [2, 4]]
    assert s.canAttendMeetings(intervals) == True
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert s.canAttendMeetings(intervals) == False
    intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert s.canAttendMeetings(intervals) == True
    intervals = [[1, 2], [2, 3]]
    assert s.canAttendMeetings(intervals) == True
    print("All tests passed")
