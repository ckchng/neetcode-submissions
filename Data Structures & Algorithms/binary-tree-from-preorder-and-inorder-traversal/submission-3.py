# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # given preorder and inorder, build a tree
        # preorder tells you which one is the root
        # inorder tells you the size of the left part
        # build a inorder hash for fast access
        if len(preorder) == 0:
            return 
        inorder_hash = {}
        for id, val in enumerate(inorder):
            inorder_hash[val] = id
        

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root = TreeNode(preorder[pre_start])
            mid = inorder_hash[preorder[pre_start]]
            left_size = mid - in_start

            root.left = helper(pre_start + 1, pre_start + left_size, in_start, in_start + left_size)
            root.right = helper(pre_start + 1 + left_size, pre_end, in_start + 1 + left_size, in_end)

            return root
        
        root = helper(0, len(preorder) - 1, 0, len(inorder) - 1) 
        return root
        
    
