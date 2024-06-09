from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Utilises Kadane's Algorithm"""
        largest = float("-inf")
        curr_largest = float("-inf")
        for val in nums:  # 1
            curr_largest = max(val, curr_largest + val)  # 1
            largest = max(curr_largest, largest)  # 1
        return largest


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
