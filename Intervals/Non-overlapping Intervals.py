from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        lst = intervals[0][1]  # latest start time
        result = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < lst:
                lst = min(interval[1], lst)
                result += 1
            else:
                lst = interval[1]
        return result


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert s.eraseOverlapIntervals(intervals) == 1
    intervals = [[1, 2], [1, 2], [1, 2]]
    assert s.eraseOverlapIntervals(intervals) == 2
    intervals = [[1, 2], [2, 3]]
    assert s.eraseOverlapIntervals(intervals) == 0
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    assert s.eraseOverlapIntervals(intervals) == 2
    intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert s.eraseOverlapIntervals(intervals) == 0
    print("All tests passed")
