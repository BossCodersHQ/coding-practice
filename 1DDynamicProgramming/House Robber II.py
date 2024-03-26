from typing import List
class Solution:
	def rob(self, nums: List[int]) -> int:
		def hr(arr: List[int]) -> int:
			rob1, rob2 = 0,0
			for num in arr:
				new_max = max(rob1 + num, rob2)
				rob1 = rob2
				rob2 = new_max
			return rob2
		
		if len(nums) == 1:
			return nums[0]
			
		hr0 = hr(nums[0:-1])
		hr1 = hr(nums[1:])
		return max(hr0, hr1)

if __name__ == "__main__":
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 11
    assert s.rob([2,3,2]) == 3