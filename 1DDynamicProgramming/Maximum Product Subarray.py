from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        curr_max_product = 1
        curr_min_product = 1
        for num in nums:
            if num == 0:
                curr_max_product = 1
                curr_min_product = 1
                max_product = max(num, max_product)
            else:
                curr_max_product, curr_min_product = max(
                    num, curr_max_product * num, curr_min_product * num
                ), min(num, curr_max_product * num, curr_min_product * num)
                max_product = max(curr_max_product, max_product)
        return max_product


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
