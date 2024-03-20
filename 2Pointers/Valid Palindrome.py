class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = {c for c in "abcdefghijklmnopqrstuvwxyz1234567890"}
        s = s.lower()
        chars = [c for c in s if c in allowed]
        f_ptr = 0
        b_ptr = len(chars) - 1
        while f_ptr < b_ptr:
            if chars[f_ptr] != chars[b_ptr]:
                return False
            f_ptr += 1
            b_ptr -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("race e car")
