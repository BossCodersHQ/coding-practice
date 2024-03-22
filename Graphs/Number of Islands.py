from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        num_groups = 0

        def dfs(i, j):
            if grid[j][i] == "0":
                return
            grid[j][i] = "0"
            if i + 1 < width:
                dfs(i + 1, j)
            if i - 1 >= 0:
                dfs(i - 1, j)
            if j + 1 < height:
                dfs(i, j + 1)
            if j - 1 >= 0:
                dfs(i, j - 1)

        for j in range(height):
            for i in range(width):
                if grid[j][i] == "0":
                    continue
                dfs(i, j)
                num_groups += 1
        return num_groups


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert s.numIslands(grid) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert s.numIslands(grid) == 3
    grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    assert s.numIslands(grid) == 1
    grid = [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]
    assert s.numIslands(grid) == 5
    grid = [["1", "0", "1"], ["0", "0", "0"], ["1", "0", "1"]]
    assert s.numIslands(grid) == 4
    grid = [["1", "0", "1"], ["0", "0", "0"], ["1", "0", "0"]]
    assert s.numIslands(grid) == 3
    grid = [["1", "0", "1"], ["0", "0", "0"], ["0", "0", "0"]]
    assert s.numIslands(grid) == 2
    grid = [["1", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    assert s.numIslands(grid) == 1
    grid = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
    assert s.numIslands(grid) == 1
    grid = [["1", "0", "1"], ["0", "0", "0"], ["1", "0", "1"]]
    assert s.numIslands(grid) == 4
    grid = [["1", "0", "1"], ["0", "0", "0"], ["1", "0", "1"]]
    assert s.numIslands(grid) == 4
    grid = [["1", "0", "1"], ["0", "0", "0"], ["1", "0", "0"]]
    assert s.numIslands(grid) == 3
    grid = [["1", "0", "1"], ["0", "0", "0"], ["0", "0", "0"]]
    assert s.numIslands(grid) == 2
    grid = [["1", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    assert s.numIslands(grid) == 1
