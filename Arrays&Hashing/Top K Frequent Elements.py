import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = collections.defaultdict(int)
        for num in nums:
            map[num] += 1
        sorted_list = list(sorted(map.items(), key=lambda x: x[1], reverse=True))
        return [key for key, val in sorted_list[:k]]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert s.topKFrequent(nums, k) == [1, 2]
    nums = [1]
    k = 1
    assert s.topKFrequent(nums, k) == [1]
    nums = [1, 2]
    k = 2
    assert s.topKFrequent(nums, k) == [1, 2]
    nums = [1, 2]
    k = 1
    assert s.topKFrequent(nums, k) == [1]
    nums = [1, 2, 3]
    k = 2
    assert s.topKFrequent(nums, k) == [1, 2]
    nums = [1, 2, 3]
    k = 3
    assert s.topKFrequent(nums, k) == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 3]
    k = 3
    assert s.topKFrequent(nums, k) == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 3]
    k = 1
    assert s.topKFrequent(nums, k) == [1]
    nums = [1, 1, 1, 2, 2, 3]
    k = 6
    assert s.topKFrequent(nums, k) == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 3]
    k = 0
    assert s.topKFrequent(nums, k) == []
    nums = [1, 1, 1, 2, 2, 3]
    k = 4
    assert s.topKFrequent(nums, k) == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 3]
    k = 5
    assert s.topKFrequent(nums, k) == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 3]
    k = 7
    assert s.topKFrequent(nums, k) == [1, 2, 3]
