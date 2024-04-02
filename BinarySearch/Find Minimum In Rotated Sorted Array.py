from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r - l > 1:
            mid = int((l + r) / 2)
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
        return nums[r] if nums[r] < nums[l] else nums[0]


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    assert s.findMin(nums) == 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert s.findMin(nums) == 0
    nums = [11, 13, 15, 17]
    assert s.findMin(nums) == 11
    nums = [1]
    assert s.findMin(nums) == 1
