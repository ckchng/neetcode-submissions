# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # DFS
        # swap everytime there is node
        if root is None:
            return root
        bin_tree = [root]
        while bin_tree:
            curr_node = bin_tree.pop() # LIFO
            if curr_node.left is not None and curr_node.right is None:
                curr_node.left, curr_node.right = None, curr_node.left
                bin_tree.append(curr_node.right)
                # bin_tree.append(curr_node.left)
            elif curr_node.left is None and curr_node.right is not None:
                curr_node.left, curr_node.right = curr_node.right, None
                # bin_tree.append(curr_node.right)
                bin_tree.append(curr_node.left)
            elif curr_node.left is not None and curr_node.right is not None:
                curr_node.left, curr_node.right = curr_node.right, curr_node.left
                bin_tree.append(curr_node.right)
                bin_tree.append(curr_node.left)

        return root
    