class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		length = len(s)
		if length<2:
			return length
		i,j = 0,1
		map = set(s[0])
		longest = 1
		while j < length:
			while s[j] in map:
				map.remove(s[i])
				i+=1
			map.add(s[j])
			j+=1
			longest = max(longest, j-i)
		return longest

if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring(" ") == 1
    assert s.lengthOfLongestSubstring("au") == 2
    assert s.lengthOfLongestSubstring("dvdf") == 3
    assert s.lengthOfLongestSubstring("abba") == 2
    assert s.lengthOfLongestSubstring("aab") == 2