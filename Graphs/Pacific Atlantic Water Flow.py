from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)

        def dfs(i: int, j: int, ocean: set, prev: int):
            coord = (j, i)
            curr = heights[j][i]
            if coord in ocean or prev > curr:
                return
            ocean.add(coord)

            if i < width - 1:
                dfs(i + 1, j, ocean, curr)
            if i > 0:
                dfs(i - 1, j, ocean, curr)
            if j < height - 1:
                dfs(i, j + 1, ocean, curr)
            if j > 0:
                dfs(i, j - 1, ocean, curr)

        pacific = set()
        atlantic = set()
        for j in range(height):
            dfs(0, j, pacific, float("-inf"))
            dfs(width - 1, j, atlantic, float("-inf"))

        for i in range(width):
            dfs(i, 0, pacific, float("-inf"))
            dfs(i, height - 1, atlantic, float("-inf"))

        combined = pacific & atlantic
        return [list(coord) for coord in combined]
