from collections import defaultdict
from typing import List
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		map = defaultdict(list)
		for s in strs:
			sorted_s = tuple(sorted(list(s)))
			map[sorted_s].append(s)
		return list(map.values())
	
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]