from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # NOTE intervals are inclusive
        stack = []
        for interval in intervals:
            stack.append(interval)
            if isOverlapping(stack[-1], newInterval):
                top = stack.pop()
                newInterval = mergeInterval(top, newInterval)
