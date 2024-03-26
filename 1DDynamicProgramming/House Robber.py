from typing import List
class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		arr = [nums[0], max(nums[1], nums[0])]
		for i in range(2,len(nums)):
			new_max = max(arr[1], arr[0] + nums[i])
			arr[0] = arr[1]
			arr[1] = new_max
		return arr[1]

if __name__ == "__main__":
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([2,1,1,2]) == 4
    assert s.rob([2,1,1,2,1]) == 4