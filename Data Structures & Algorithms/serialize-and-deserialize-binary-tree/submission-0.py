# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out_str = ''
        # do DFS, # do preorder, ie, root -> left -> right
        # base case:
        if root is None:
            return 'null,'
        
        out_str = out_str + str(root.val) + ','
        out_str += self.serialize(root.left)
        out_str += self.serialize(root.right)

        return out_str

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # Build the tree back with pre-order
        data = data.split(',')  # e.g. "1,2,null,null," -> ['1','2','null','null','']
        
        def helper(data):
            if not data or data[0] == 'null':
                data.pop(0)
                return None

            bin_tree = TreeNode(int(data[0]))
            data.pop(0)
            bin_tree.left = helper(data)
            bin_tree.right = helper(data)
            return bin_tree

        return helper(data)