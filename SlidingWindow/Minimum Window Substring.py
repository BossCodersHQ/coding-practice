from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(sub: dict, window: dict):
            for key in window:
                if key not in sub or window[key] > sub[key]:
                    return False
            return True

        if s == t:
            return s
        minSub = (
            0,
            len(s) + 1,
        )  # Stores index of first and last index of substring inclusive
        window = Counter(t)  # A:1,B:1,C:1

        for i in range(len(s)):  # 0
            base = s[i : i + len(t) - 1]  # s[0,2] = AD
            counter = Counter(base)  # A:1,D:1,O:1,B:1,E:1

            # Start loop from the minimum width of the window
            for j in range(i + len(t) - 1, len(s)):  # 4
                counter[s[j]] = counter.get(s[j], 0) + 1  # counter[E] = 1
                if valid(counter, window):
                    windowLength = j - i + 1
                    minSubLength = minSub[1] - minSub[0] + 1
                    minSub = minSub if minSubLength <= windowLength else (i, j)

        return s[minSub[0] : minSub[1] + 1] if minSub[1] < len(s) else ""
