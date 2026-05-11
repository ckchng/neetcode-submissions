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
        # store the tree in a preorder fashion
        # root -> left -> right
        out = ""

        def dfs_preorder(root):
            nonlocal out
            if root is None:
                out += 'null,'
                return 
            
            out += str(root.val)
            out += ','
            dfs_preorder(root.left)
            dfs_preorder(root.right)
        
        dfs_preorder(root)
        return out

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        data = data[0:-1]        
        data_id = 0
        def dfs_preorder():
            nonlocal data_id
            if data_id >= len(data):
                return
            if data[data_id] == 'null':
                data_id += 1
                return None
            
            root = TreeNode(int(data[data_id]))
            data_id += 1
            root.left = dfs_preorder()
            root.right = dfs_preorder()
            return root
        return dfs_preorder()