from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        ni = newInterval
        # binary search to find point where to start
        l, r = 0, len(intervals)
        while r - l > 1:
            m = int((l + r) / 2)
            val = intervals[m][0]
            if ni[0] >= val:
                l = m
            else:
                r = m
        result = intervals[:l]

        for i in range(l, len(intervals)):
            curr = intervals[i]
            # Check if overlapping
            if curr[0] <= ni[1] and curr[1] >= ni[0]:
                ni = [min(curr[0], ni[0]), max(curr[1], ni[1])]
            else:
                # If this is where to add the overlap
                if ni[1] < curr[0]:
                    result.append(ni)
                    result.extend(intervals[i:])
                    return result
                else:
                    result.append(curr)
        result.append(ni)
        return result


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    assert s.insert(intervals, newInterval) == [[1, 5], [6, 9]]
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    assert s.insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]]
    intervals = []
    newInterval = [5, 7]
    assert s.insert(intervals, newInterval) == [[5, 7]]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    assert s.insert(intervals, newInterval) == [[1, 5]]
    intervals = [[1, 5]]
    newInterval = [2, 7]
    assert s.insert(intervals, newInterval) == [[1, 7]]
