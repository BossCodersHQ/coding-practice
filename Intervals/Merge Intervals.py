from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlapping(a, b):
            return a[0] <= b[1] and a[1] >= b[0]

        def mergeIntervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        intervals.sort(key=lambda x: x[0])
        new_intervals = []
        buffer = intervals[0]
        for interval in intervals:
            if isOverlapping(buffer, interval):
                buffer = mergeIntervals(buffer, interval)
            else:
                new_intervals.append(buffer)
                buffer = interval
        new_intervals.append(buffer)
        return new_intervals


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert s.merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert s.merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
