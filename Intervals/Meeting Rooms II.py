from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not rooms:
                rooms.append(interval[1])
                continue
            added = False
            for i in range(len(rooms)):
                room = rooms[i]
                if interval[0] >= room:
                    rooms[i] = interval[1]
                    added = True
                    break
            if not added:
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
