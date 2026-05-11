# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # do DFS, if different number at any point, return false

        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None) or (p.val != q.val):
            # return
        # elif :
            return False
        
        equalFlag = self.isSameTree(p.left, q.left)
        if equalFlag is False:
            return False
        equalFlag = self.isSameTree(p.right, q.right)

        return equalFlag