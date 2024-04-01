from typing import List


delimiter = "#"


class Solution:
    def encode(self, strs: List[str]) -> str:
        strs = [f"{len(s)}{delimiter}{s}" for s in strs]
        print("".join(strs))
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        suffix_length = 0
        prefix_stage = True
        prefix = ""
        suffix = ""
        ret = []
        for c in s:
            if prefix_stage:
                if c == delimiter:
                    prefix_stage = False
                    suffix_length = int(prefix)
                    if suffix_length == 0:
                        ret.append(suffix)
                        prefix_stage = True
                    prefix = ""
                else:
                    prefix += c
                continue

            suffix += c
            suffix_length -= 1

            if suffix_length <= 0:
                ret.append(suffix)
                prefix_stage = True
                suffix = ""

        return ret


if __name__ == "__main__":
    s = Solution()
    strs = ["hello", "world"]
    assert s.decode(s.encode(strs)) == strs
    strs = ["hello", "world", "this is a test"]
    assert s.decode(s.encode(strs)) == strs
