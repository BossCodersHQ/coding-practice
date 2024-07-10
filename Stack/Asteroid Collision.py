from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def opposite(i, j):
            return (i > 0 and j < 0) or (j > 0 and i < 0)

        stack = []  # []
        skip = False
        for ast in asteroids:  # -50
            while stack and opposite(ast, stack[-1]):
                prev = stack.pop()  # 30
                if abs(ast) == abs(prev):
                    skip = True
                else:
                    ast = ast if abs(ast) > abs(prev) else prev
            if not skip:
                stack.append(ast)  # [-50]
            skip = False
        return stack

if __name__ == "__main__":
    solution = Solution()
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]
    assert solution.asteroidCollision([8, -8]) == []
    assert solution.asteroidCollision([10, 2, -5]) == [10]
    assert solution.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert solution.asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2]
    print("Passed all test cases!")