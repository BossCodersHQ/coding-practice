from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def cs(curr: List[int], new_target: int, results: set, level: int):
            if new_target == 0:
                results.add(tuple(sorted(curr)))
                return
            for val in candidates:
                if new_target - val >= 0:
                    cs(curr + [val], new_target - val, results, level + 1)

        ret = set()
        cs([], target, ret, 0)
        return [list(vals) for vals in ret]


if __name__ == "__main__":
    # Very flaky testing, i know :)
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum([2], 1) == []
    assert Solution().combinationSum([1], 1) == [[1]]
    assert Solution().combinationSum([1], 2) == [[1, 1]]
