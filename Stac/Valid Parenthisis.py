class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		open_b = "({["
		close_b = ")}]"
		match = {a:b for a,b in zip(open_b, close_b)}
		for char in s:
			if char in close_b:
				if len(stack) == 0:
					return False
				open = stack.pop()
				if match[open] != char:
					return False
			else:
				stack.append(char)
		return True if len(stack) == 0 else False