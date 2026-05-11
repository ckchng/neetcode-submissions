class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                # initialising a dict and setting a value to it at the same time
                node.children[c] = TrieNode()
            node = node.children[c]
            
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True