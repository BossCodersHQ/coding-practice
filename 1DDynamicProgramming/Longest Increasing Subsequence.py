from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):  # 1
            longest = 1
            for j in range(i + 1, len(nums)):  # 2
                if nums[j] > nums[i]:
                    longest = max(longest, 1 + dp[j])
            dp[i] = longest
        return max(dp)


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
