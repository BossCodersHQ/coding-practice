from typing import Optional

from tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(Solution().isValidBST(root))

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(Solution().isValidBST(root))
