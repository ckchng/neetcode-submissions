# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create the root node
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        # first find the root node in inorder. It's equivalent to the first node in preorder
        for root_id, node in enumerate(inorder):
            if node == preorder[0]:
                break

        # since everything to the left of the root in inorder will be the left-subtree, chop them to half
        # Go down each sub-tree, and do everything again, i.e., find the root in the sub-trees, and slice them to form left and right sub-trees
        root.left = self.buildTree(preorder[1:root_id+1] , inorder[0:root_id])
        root.right = self.buildTree(preorder[root_id+1:] , inorder[root_id+1:])

        return root
    
