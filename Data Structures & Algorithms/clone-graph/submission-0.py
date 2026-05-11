"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        
        seen = {}

        def helper(node):
            # if it's already in seen, return the clone
            if node in seen:
                return seen[node] # which is the clone version, stopping the recursion and hence avoid recycling
            
            clone = Node(node.val)
            seen[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(helper(neighbor))
            
            return clone
        
        return helper(node)