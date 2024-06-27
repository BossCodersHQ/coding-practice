from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(sub: dict, window: dict):
            for key, val in window.items():
                if key not in sub:
                    return False
                sub[key] -= val
                if sub[key] < 0:
                    return False
            return True

        if s == t:
            return s
        minSub = s
        window = Counter(t)

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                sub = s[i : j + 1]
                if valid(Counter(sub), window):
                    minSub = sub if len(sub) < len(minSub) else minSub

        if minSub == s:
            return ""
        return minSub
