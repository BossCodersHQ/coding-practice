from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = -float("inf")
        curr_max = 1
        curr_min = 1
        for num in nums:
            curr_max, curr_min = max(curr_max * num, num, curr_min * num), min(
                curr_min * num, num, curr_max * num
            )
            ret = max(curr_max, ret)
        return ret


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
