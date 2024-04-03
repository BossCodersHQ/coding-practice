from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find rotation point by finding lowest number
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        l, r = 0, len(nums) - 1
        alreadysorted = nums[l] < nums[r]

        while r - l > 1 and not alreadysorted:
            mid = int((l + r) / 2)
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
        k = r

        def bs(l: int, r: int) -> int:
            while r - l > 1:
                mid = int((l + r) / 2)
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid

            if target == nums[l]:
                return l
            if target == nums[r]:
                return r

            return -1

        if nums[0] <= target and target <= nums[k - 1]:
            return bs(0, k - 1)
        elif nums[k] <= target and target <= nums[-1]:
            return bs(k, len(nums) - 1)
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert s.search(nums, target) == 4
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert s.search(nums, target) == -1
    nums = [1]
    target = 0
    assert s.search(nums, target) == -1
    nums = [1]
    target = 1
    assert s.search(nums, target) == 0
    nums = [3, 4, 5, 1, 2]
    target = 1
    assert s.search(nums, target) == 3
