class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        window = len(s1)  # 2
        counts = Counter(s1)  # {a:1, b:1}
        if len(s1) > len(s2):
            return False
        if s1 == "":
            return True
        curr_counts = Counter(s2[0:window])  # s2[0,2] = "ei" // {e:1,b:1}
        if curr_counts == counts:
            return True
        for i in range(window, len(s2)):  # 2
            char = s2[i]  # d
            old_char = s2[i - window]  # s2[0] = e
            curr_counts[char] = curr_counts.get(char, 0) + 1  # {e:1,b:1,d:1}
            curr_counts[old_char] -= 1
            if curr_counts.get(old_char) == 0:
                del curr_counts[old_char]

            if curr_counts == counts:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("a", "a") == True
    assert s.checkInclusion("a", "b") == False
    assert s.checkInclusion("a", "") == False
