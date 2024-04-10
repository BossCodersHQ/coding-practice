class Solution:
	def hammingWeight(self, n: int) -> int:
		setbits = 0
		while n>0:
			if n & 1 != 0:
				setbits +=1
			n = n >> 1
		return setbits

if __name__ == "__main__":
    assert Solution().hammingWeight(0b00000000000000000000000000001011) == 3
    assert Solution().hammingWeight(0b00000000000000000000000010000000) == 1