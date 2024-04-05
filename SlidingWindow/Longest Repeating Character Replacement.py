class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		map = {}
		maxf = 0
		i = 0
		for j in range(len(s)):
			map[s[j]] = 1 + map.get(s[j], 0)
			maxf = max(maxf, map[s[j]])
			while (j-i + 1) - maxf > k:
				map[s[i]] -= 1
				i += 1
			
		return min(maxf + k, len(s))
	
if __name__ == "__main__":
    assert(Solution().characterReplacement("ABAB", 2) == 4)
    assert(Solution().characterReplacement("AABABBA", 1) == 4)
    assert(Solution().characterReplacement("AABA", 0) == 2)
    assert(Solution().characterReplacement("AAAA", 0) == 4)