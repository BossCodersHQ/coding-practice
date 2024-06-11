from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        needed = 1
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= needed:
                needed = 1
                continue
            else:
                needed += 1

        return needed <= 1


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
    assert s.canJump([0]) == True
