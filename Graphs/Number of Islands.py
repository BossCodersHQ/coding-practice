from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        def bfs(col, row):
            q = deque()
            q.appendleft((col,row))
            while q:
                c, r = q.pop()
                if (
                    c < 0
                    or c >= len(grid)
                    or r < 0
                    or r >= len(grid[0])
                    or grid[c][r] == "0"
                ):
                    continue

                grid[c][r] = "0"
                q.appendleft((c + 1, r))
                q.appendleft((c - 1, r))
                q.appendleft((c, r + 1))
                q.appendleft((c, r - 1))

        count = 0
        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[c][r] == "0":
                    continue
                count += 1
                bfs(c, r)
        return count



if __name__ == "__main__":
    s = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert s.numIslands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert s.numIslands(grid2) == 3

    grid3 = [
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
    ]
    assert s.numIslands(grid3) == 10
