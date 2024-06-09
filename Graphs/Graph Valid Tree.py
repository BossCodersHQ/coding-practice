from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(curr: int, prev: int) -> bool:
            """Returns True if no cycles"""
            if curr in visited:
                return False

            visited.add(curr)

            for neighbour in adj_list[curr]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, curr):
                    return False

            return True

        return dfs(0, 0) and len(visited) == n


if __name__ == "__main__":
    numCourses = 5
    prerequisites = [[0, 1], [0, 2], [0, 3], [1, 4]]
    s = Solution()
    assert s.validTree(numCourses, prerequisites) == True

    numCourses = 5
    prerequisites = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    s = Solution()
    assert s.validTree(numCourses, prerequisites) == False
