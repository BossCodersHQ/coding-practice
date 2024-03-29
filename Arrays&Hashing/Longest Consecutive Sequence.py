from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        top = bottom = nums[0]
        for num in nums:
            if num < bottom:
                bottom = num
            if num > top:
                top = num

        length = top - bottom + 1
        arr = [False] * length
        offset = 0 - bottom
        for num in nums:
            arr[num + offset] = True

        max_count = 0
        i = j = 0
        while i < length:
            while j < length and arr[j]:
                j += 1
            max_count = max(max_count, j - i)
            i = j + 1
            j = i
        return max_count


if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    assert s.longestConsecutive(nums) == 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert s.longestConsecutive(nums) == 9
    nums = [1, 2, 0, 1]
    assert s.longestConsecutive(nums) == 3
