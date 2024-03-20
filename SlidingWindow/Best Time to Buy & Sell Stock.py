from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if len(prices) == 1:
			return 0
		start = 0
		max_profit = 0
		while start < len(prices):
			end = start + 1
			while end < len(prices) and prices[end] > prices[start]:
				max_profit = max(prices[end] - prices[start], max_profit)
				end += 1
			start = end
		return max_profit
	
if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([1,2]) == 1
    assert s.maxProfit([2,1]) == 0
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1,2,3,4,5]) == 4
    assert s.maxProfit([7,1,5,3,6,4,7]) == 6
    assert s.maxProfit([7,1,5,3,6,4,7,2,9]) == 8
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10]) == 9
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11]) == 10
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11,1,12]) == 11
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11,1,12,1,13]) == 12
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11,1,12,1,13,1,14]) == 13
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11,1,12,1,13,1,14,1,15]) == 14
    assert s.maxProfit([7,1,5,3,6,4,7,2,9,1,10,1,11,1,12,1,13,1,14,1,15,1,16]) == 15