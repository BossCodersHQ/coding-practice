from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, arr):
            if i == len(nums):
                return len(arr)

            with_i = 0
            last_num = float("-inf") if len(arr) == 0 else arr[-1]

            if nums[i] > last_num:
                arr.append(nums[i])
                with_i = dfs(i + 1, arr)
                arr.pop()

            without_i = dfs(i + 1, arr)

            return max(with_i, without_i)

        return dfs(0, [])


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    assert s.lengthOfLIS(nums) == 4
    nums = [0, 1, 0, 3, 2, 3]
    assert s.lengthOfLIS(nums) == 4
    nums = [7, 7, 7, 7, 7, 7, 7]
    assert s.lengthOfLIS(nums) == 1
    nums = [4, 10, 4, 3, 8, 9]
    assert s.lengthOfLIS(nums) == 3
