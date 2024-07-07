class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == "":
            return True

        from collections import Counter

        window = len(s1)
        s1map = Counter(s1)
        s2map = Counter(s2[0:window])

        matches = 0
        for i in range(0, 26):
            c = chr(ord("a") + i)
            if s1map.get(c, 0) == s2map.get(c, 0):
                matches += 1

        for i in range(window, len(s2)):  # 2
            if matches == 26:
                return True
            char = s2[i]  # d

            s2map[char] = s2map.get(char, 0) + 1  # {e:1,b:1,d:1}

            if s1map.get(char, 0) == s2map[char]:
                matches += 1
            elif s1map.get(char, 0) == s2map[char] - 1:
                matches -= 1

            old_char = s2[i - window]  # s2[0] = e
            s2map[old_char] -= 1

            if s1map.get(old_char, 0) == s2map[old_char]:
                matches += 1
            elif s1map.get(old_char, 0) == s2map[old_char] + 1:
                matches -= 1

        return matches == 26


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("a", "a") == True
    assert s.checkInclusion("a", "b") == False
    assert s.checkInclusion("a", "") == False
