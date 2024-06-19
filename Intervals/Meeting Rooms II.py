from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []
        for interval in intervals:
            need_room = True
            for i in range(len(rooms)):
                earliest = rooms[i]
                if interval[0] >= earliest:
                    rooms[i] = interval[1]
                    need_room = False
                    break
            if need_room:
                rooms.append(interval[1])
        return len(rooms)


if __name__ == "__main__":
    s = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert s.minMeetingRooms(intervals) == 2
    intervals = [[7, 10], [2, 4]]
    assert s.minMeetingRooms(intervals) == 1
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert s.minMeetingRooms(intervals) == 2
    intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert s.minMeetingRooms(intervals) == 1
    intervals = [[1, 2], [2, 3]]
    assert s.minMeetingRooms(intervals) == 1
    print("All tests passed")
