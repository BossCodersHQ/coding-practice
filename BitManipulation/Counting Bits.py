from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)
        count = mult = 1
        for i in range(1, n + 1):
            if count == 0:
                mult *= 2
                count = mult
            dp[i] = 1 + dp[i - mult]
            count -= 1
        return dp


if __name__ == "__main__":
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
