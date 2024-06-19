from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        def dfs(node):
            if not node:
                return None, None
            if not node.child and not node.next:
                return node, node
            if not node.child:
                front, back = dfs(node.next)
                node.next = front
                front.prev = node
                return node, back

            if not node.next:
                front, back = dfs(node.child)
                node.next = front
                front.prev = node
                node.child = None
                return node, back

            child_front, child_back = dfs(node.child)
            next_front, next_back = dfs(node.next)

            child_back.next = next_front
            next_front.prev = child_back

            node.child = None
            node.next = child_front
            child_front.prev = node

            return node, next_back

        front, back = dfs(head)
        return front
