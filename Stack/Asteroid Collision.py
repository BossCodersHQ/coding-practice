from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for nxt in asteroids:
            while nxt and nxt < 0 and stack and stack[-1] > 0:
                pop = stack.pop()
                if abs(pop) == abs(nxt):
                    nxt = None
                elif abs(pop) > abs(nxt):
                    nxt = pop
                else:
                    nxt = nxt
            if nxt:
                stack.append(nxt)
        return stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]
    assert solution.asteroidCollision([8, -8]) == []
    assert solution.asteroidCollision([10, 2, -5]) == [10]
    assert solution.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert solution.asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2]
    print("Passed all test cases!")
