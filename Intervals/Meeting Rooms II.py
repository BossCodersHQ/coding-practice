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


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))

        times.sort(key=lambda x: (x[0], x[1]))

        max_count = count = 0
        for time, c in times:
            if c == 1:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
        return max_count


if __name__ == "__main__":
    s = Solution2()
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
