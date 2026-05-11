# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(node):
            if node is None:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0) # the zero here is important because when you do bending, you might not want to add the negative branch
            res[0] = max(res[0], node.val + left + right) # bending

            return node.val + max(left, right)
        
        dfs(root)
        return res[0]