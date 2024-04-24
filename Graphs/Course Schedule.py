from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        adjlist = defaultdict(list)
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)

        visited = set()

        def dfs(course: int):
            """Return true if you can finish coures"""
            if course not in adjlist:
                return True
            if course in visited:
                return False

            visited.add(course)
            for prereq in adjlist[course]:
                if not dfs(prereq):
                    return False

            del adjlist[course]
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    s = Solution()
    assert s.canFinish(numCourses, prerequisites)  == True

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    s = Solution()
    assert s.canFinish(numCourses, prerequisites) == False