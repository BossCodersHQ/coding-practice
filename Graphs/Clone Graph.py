from typing import Optional
class Node:
	def __init__(self, val = 0, neighbors = []):
		self.val = val
		self.neighbors = neighbors

class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		return self.cgr(node, {}) if node else None

	def cgr(self, node: Optional['Node'],visited: dict) -> Optional['Node']:
		if node in visited:
			return visited[node]
		new_node = Node(node.val)
		visited[node] = new_node
		for neighbor in node.neighbors:
			new_node.neighbors.append(self.cgr(neighbor, visited))
		return new_node

if __name__ == "__main__":
	node = Node(1)
	node.neighbors = [Node(2), Node(3)]
	node.neighbors[0].neighbors = [node, Node(3)]
	node.neighbors[1].neighbors = [node, Node(2)]
	s = Solution()
	print(s.cloneGraph(node))