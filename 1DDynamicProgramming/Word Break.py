from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[0] = True
        for i in range(len(s)):  # 4
            for word in wordDict:  # leet
                l = i - len(word) + 1  # 1
                if l < 0:
                    continue
                if s[l : i + 1].startswith(word) and memo[l]:  #
                    memo[i + 1] = memo[i + 1] or True
                else:
                    memo[i + 1] = memo[i + 1] or False
        return memo[len(s)]


if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) == True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert s.wordBreak("cars", ["car", "ca", "rs"]) == True
