from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not rooms:
                heapq.heappush(rooms, interval[1])
                continue
            room = heapq.heappop(rooms)
            if interval[0] >= room:
                heapq.heappush(rooms, interval[1])
            else:
                heapq.heappush(rooms, room)
                heapq.heappush(rooms, interval[1])

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
