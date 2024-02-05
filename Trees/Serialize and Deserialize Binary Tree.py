from tree_node import TreeNode
from collections import deque
NULL_NODE = "N"
class Codec:

    def serialize(self, root: TreeNode)->str:
        q = deque([root])
        ret = []
        while q:
            found_non_leaf_node = False
            for _ in range(len(q)):
                curr = q.popleft()
                ret.append(str(curr.val) if curr else NULL_NODE)
                if not curr:
                    continue
                if curr.left or curr.right:
                    found_non_leaf_node = True
                q.append(curr.left)
                q.append(curr.right)
            if not found_non_leaf_node:
                break
        return "".join(ret)

    def deserialize(self, data:str) -> TreeNode:
        # If a node is at index i its children are at index (2*i)+1 & (2*i) +2
        node_data = [TreeNode(val) if val != NULL_NODE else None for val in data]
        print(len(node_data))
        i = 0
        while (2*i)+2 < len(node_data):
            curr = node_data[i]
            if not curr:
                i+=1
                continue
            first_child_index = (2*i) + 1
            curr.left = node_data[first_child_index]
            curr.right = node_data[first_child_index + 1]
            i+=1
        return node_data[0]
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    codec = Codec()
    serialized = codec.serialize(root)
    print(serialized)
    deserialized = codec.deserialize(serialized)
    assert(codec.serialize(deserialized) == serialized)