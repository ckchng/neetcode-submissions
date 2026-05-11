
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first add the words in Trie
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()    
                node = node.children[c]
                
            node.is_end = True
    
        options = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        res = []
        current = []

        def backtrack(r, c, current, node):
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return
            if board[r][c] not in node.children:
                return
            if (r, c) in visited:
                return
            
            current.append(board[r][c])
            visited.add((r, c))

            next_node = node.children[board[r][c]]
            if next_node.is_end:
                res.append("".join(current))
                next_node.is_end = False
                

            for option in options:
                backtrack(r + option[0], c + option[1], current, next_node)

            current.pop()
            visited.remove((r, c))

            if not next_node.children: # if there is no more children, that means we already found it
                del node.children[board[r][c]]

            return
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    backtrack(r, c, current, root)
        return res