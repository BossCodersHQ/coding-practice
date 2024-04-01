from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for c in nums:
            if c in s:
                return True
            s.add(c)
        return False
