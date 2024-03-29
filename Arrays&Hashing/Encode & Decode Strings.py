from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        def escape(string):
            return string

        final = []
        for s in strs:
            final.append(f'"{escape(s)}"')
        return ",".join(final)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        s = s[1:-1]
        return s.split('","')


if __name__ == "__main__":
    s = Solution()
    strs = ["hello", "world"]
    assert s.decode(s.encode(strs)) == strs
    strs = ["hello", "world", "this is a test"]
    assert s.decode(s.encode(strs)) == strs
