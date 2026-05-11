# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # handle exception cases here
        q = [[root, 1]]
        max_d = 0
        while q:
            curr_node, curr_depth = q.pop()
            max_d = max(curr_depth, max_d)

            # if left exists
            if curr_node.left is not None:
                q.append([curr_node.left, curr_depth + 1])
            if curr_node.right is not None:    
                q.append([curr_node.right, curr_depth + 1])

        return max_d 