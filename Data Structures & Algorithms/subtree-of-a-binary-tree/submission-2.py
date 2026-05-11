# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):            
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # dfs the root, if found a same node, run isSameTree
        if root is None:
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)