from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		i,j = 0, len(height)-1
		largest = 0
		while i<j:
			h_i, h_j = height[i], height[j]
			area = min(h_i, h_j) * abs(i-j)
			largest = max(largest, area)
			if h_i < h_j:
				i+=1
			else:
				j-=1
		return largest

if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    assert s.maxArea(height) == 49
    height = [1,1]
    assert s.maxArea(height) == 1
    height = [4,3,2,1,4]
    assert s.maxArea(height) == 16
    height = [1,2,1]
    assert s.maxArea(height) == 2
    height = [1,2,3,4,5,25,24,3,4]
    assert s.maxArea(height) == 24