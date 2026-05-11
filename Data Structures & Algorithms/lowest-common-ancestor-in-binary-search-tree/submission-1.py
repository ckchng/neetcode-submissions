# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # base case
        if q.val > p.val:
            if p.val <= root.val <= q.val:
                return root
            elif root is None:
                return root
            elif root.val >= p.val and root.val >= q.val:
                root = self.lowestCommonAncestor(root.left, p, q)
            elif root.val <= p.val and root.val <= q.val:
                root = self.lowestCommonAncestor(root.right, p, q)
        else:
            if q.val <= root.val <= p.val:
                return root
            elif root is None:
                return root
            elif root.val >= p.val and root.val >= q.val:
                root = self.lowestCommonAncestor(root.left, p, q)
            elif root.val <= p.val and root.val <= q.val:
                root = self.lowestCommonAncestor(root.right, p, q)

        return root