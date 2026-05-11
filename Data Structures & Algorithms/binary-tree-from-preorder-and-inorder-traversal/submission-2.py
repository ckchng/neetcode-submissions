# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first, we build an inorder hash
        if len(preorder) == 0:
            return None
        inorder_hash = {}
        for id, val in enumerate(inorder):
            inorder_hash[val] = id

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end: # termination case
                return None
            
            root = TreeNode(preorder[pre_start])
            
            mid = inorder_hash[preorder[pre_start]]
            left_size =  mid - in_start 

            root.left = helper(pre_start+1, pre_start + left_size, in_start, in_start + left_size)
            root.right = helper(pre_start+1+left_size, pre_end, in_start+left_size+1, in_end)

            return root


        return helper(0, len(preorder) -1, 0, len(inorder)-1)
        
    
