from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = [1] * length
        # Calculating prefixes
        for i in range(length - 2, -1, -1):
            ret[i] = nums[i + 1] * ret[i + 1]
        # Calculating suffixes
        for i in range(1, length):
            nums[i] = nums[i] * nums[i - 1]
            ret[i] = nums[i - 1] * ret[i]
        return ret


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    assert s.productExceptSelf(nums) == [24, 12, 8, 6]
    nums = [1, 2, 3, 4, 5]
    assert s.productExceptSelf(nums) == [120, 60, 40, 30, 24]
    nums = [1, 2, 3, 4, 5, 6]
    assert s.productExceptSelf(nums) == [720, 360, 240, 180, 144, 120]
    nums = [1, 2, 3, 4, 5, 6, 7]
    assert s.productExceptSelf(nums) == [5040, 2520, 1680, 1260, 1008, 840, 720]
