from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(count: int, arr: List[int], curr: int):
            if count < 0 or curr >= len(candidates):
                return
            if count == 0:
                ret.append(arr)
                return

            # Choosing curr
            val = candidates[curr]
            dfs(count - val, arr + [val], curr)

            # Not Choosing curr & moving to next place
            dfs(count, arr, curr + 1)

        dfs(target, [], 0)
        return ret


if __name__ == "__main__":
    # Very flaky testing, i know :)
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum([2], 1) == []
    assert Solution().combinationSum([1], 1) == [[1]]
    assert Solution().combinationSum([1], 2) == [[1, 1]]
