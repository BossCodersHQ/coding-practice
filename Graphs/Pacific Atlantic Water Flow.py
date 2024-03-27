from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        pac_set = {(0, i) for i in range(width)} | {(j, 0) for j in range(height)}
        atl_set = {(height - 1, i) for i in range(width)} | {
            (j, width - 1) for j in range(height)
        }
        adj_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()

        def dfs(y: int, x: int):
            coord = (y, x)
            if coord in visited:
                return
            visited.add(coord)
            for adj in adj_list:
                new_coord = (coord[0] + adj[0], coord[1] + adj[1])
                if (
                    new_coord[0] >= height
                    or new_coord[0] < 0
                    or new_coord[1] >= width
                    or new_coord[1] < 0
                ):
                    continue
                if heights[new_coord[0]][new_coord[1]] < heights[coord[0]][coord[1]]:
                    continue
                dfs(new_coord[0], new_coord[1])
                if new_coord in pac_set:
                    pac_set.add(coord)
                if new_coord in atl_set:
                    atl_set.add(coord)

        for j in range(height):
            for i in range(width):
                dfs(j, i)

        return list(pac_set & atl_set)

# This solution is currently not working