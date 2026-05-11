# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at every node, check if it's within range
        def dfs(root, min, max):
            if root is None:    
                return True
            if root.val < max and root.val > min:
                return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
            else:
                return False
    
        return dfs(root, -1001, float('inf'))