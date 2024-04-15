from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        for ix, num in enumerate(nums):
            ret ^= ix ^ num
        ret ^= len(nums)
        return ret


if __name__ == "__main__":
    sol = Solution()
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert sol.missingNumber([0]) == 1
    assert sol.missingNumber([1]) == 0
