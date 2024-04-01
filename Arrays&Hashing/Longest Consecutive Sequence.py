from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in map:
                continue
            # If it's the start of a sequence
            next_num = num
            while next_num in map:
                next_num += 1

            longest = max(longest, next_num - num)
        return longest


if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    assert s.longestConsecutive(nums) == 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert s.longestConsecutive(nums) == 9
    nums = [1, 2, 0, 1]
    assert s.longestConsecutive(nums) == 3
