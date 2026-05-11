# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: 
            return []
        
        out = []
        
        level = 1
        stored = 1
        q = [root]
        # the update is level = level * 2
        while q:
            i = 0
            curr_stored = 0
            curr_level = []
            while i < level and i < stored and q:
                curr_node = q.pop(0) # FIFO
                if curr_node is not None:
                    curr_level.append(curr_node.val)
                    if curr_node.left:
                        q.append(curr_node.left)
                        curr_stored += 1
                    if curr_node.right:
                        q.append(curr_node.right)
                        curr_stored += 1
                i+=1
            stored = curr_stored
            out.append(curr_level)
            level *= 2

        return out