from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        length = len(nums)
        ret = []
        nums.sort()
        while nums[i] <= 0 and i < length - 2:
            # Skip when starting from the same value as this will result in duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = length - 1
            target = 0 - nums[i]

            while j < k:
                curr = nums[j] + nums[k]
                if curr <= target:
                    if curr == target:
                        ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Loop until you get to a new number
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                else:
                    k -= 1

            # Move counter forward
            i += 1
        return ret


def main():
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
