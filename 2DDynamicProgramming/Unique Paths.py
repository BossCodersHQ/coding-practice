class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] *m
        # All cols on bottom row have one way
        for j in range(n):
            dp[m-1][j] = 1

        # All rows on last column have one way
        for i in range(m):
            dp[i][n-1] = 1
        
        # Looping through all cells
        for i in range(m-2,-1,-1): # 0
            for j in range(n-2,-1,-1): # 0
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(7, 3) == 28
    assert s.uniquePaths(3, 3) == 6
    assert s.uniquePaths(3, 4) == 10
    assert s.uniquePaths(4, 3) == 10
    assert s.uniquePaths(4, 4) == 20
    assert s.uniquePaths(4, 5) == 35
    assert s.uniquePaths(5, 4) == 35
    assert s.uniquePaths(5, 5) == 70
    assert s.uniquePaths(5, 6) == 126
    assert s.uniquePaths(6, 5) == 126
    assert s.uniquePaths(6, 6) == 252