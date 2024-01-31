from typing import Optional
from tree_node import TreeNode

def iterative_in_order(root: Optional[TreeNode]):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr = stack.pop()
        print(curr.val)
        curr=curr.right
    

		
if __name__ == "__main__":
    # root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)

    # iterative_in_order(root)

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    iterative_in_order(root)