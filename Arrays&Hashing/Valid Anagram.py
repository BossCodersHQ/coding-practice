class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for c in s:
            counts[c] = 1 + counts.get(c,0)
        
        for c in t:
            if c not in counts:
                return False
            counts[c] -= 1
        
        for character,count in counts.items():
            if count!=0:
                return False

        return True

if 