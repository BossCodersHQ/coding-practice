class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0 for i in range(n + 1)]
        results[0] = 1
        results[1] = 1
        for i in range(2, n + 1):
            results[i] = results[i - 2] + results[i - 1]
            print(i, results[i - 2], results[i - 1])
        return results[n]


if __name__ == "__main__":
    # test climbStairs
    sol = Solution()
    assert(sol.climbStairs(2) == 2)
    assert(sol.climbStairs(3) == 3)
    assert(sol.climbStairs(4) == 5)
    assert(sol.climbStairs(5) == 8)
    print("all tests passed.")