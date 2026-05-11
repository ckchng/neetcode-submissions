# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            elif (p is not None and q is not None) and (p.val == q.val):
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            # elif 
            else:
                return False   
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # base_case
        if root is None:
            return False
        elif root.val == subRoot.val:
            if (self.isSameTree(root, subRoot)):
                return True
            else: 
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)