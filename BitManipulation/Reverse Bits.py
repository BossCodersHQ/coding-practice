class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            val = n & 1
            reverse |= val
            if i == 31:
                break
            n >>= 1
            reverse <<= 1
        return reverse


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseBits(0b00000010100101000001111010011100) == 964176192
