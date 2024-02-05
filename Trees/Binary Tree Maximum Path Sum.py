from typing import Optional
from tree_node import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(node, max_l:list) -> int:
            if not node:
                return float("-inf")
            left_path = maxPath(node.left, max_l)
            right_path = maxPath(node.right, max_l)

            full_path = left_path + node.val + right_path
            left_path_and_curr = left_path + node.val
            right_path_and_curr = right_path + node.val
            
            curr_node_total = max(left_path_and_curr, right_path_and_curr, node.val)
            new_max = max(curr_node_total, full_path)

            if new_max>max_l[0]:
                print("changing max", new_max)
                max_l[0] = new_max
            return curr_node_total
        l = [float("-inf")]
        maxPath(root, l)
        return l[0]
    
if __name__ == "__main__":
    # root = TreeNode(1, TreeNode(2), TreeNode(3))
    # print(Solution().maxPathSum(root))  # 6
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxPathSum(root))  # 42