# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            #create a queue with range and node
            q = []
            
            q = [[root, [-float("infinity"), float("infinity")]]]

            while q:
                curr_node, curr_range = q.pop()

                if curr_range[0] < curr_node.val and curr_node.val < curr_range[1]:
                    # branch left
                    if curr_node.left:
                        q.append([curr_node.left, [curr_range[0], curr_node.val]])
                    
                    if curr_node.right:
                        q.append([curr_node.right, [curr_node.val, curr_range[1]]])
                else:
                    return False
            
            return True