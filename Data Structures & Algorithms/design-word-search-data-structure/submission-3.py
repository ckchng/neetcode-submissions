class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:


    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_end = True

    def search(self, word: str) -> bool:
        # we need a dfs
        node = self.root
        
        def dfs(node, word_id):
            if word_id >= len(word):
                return node.is_end
            
            if word[word_id] not in node.children and word[word_id] != '.':
                return False
            
            if word[word_id] == '.':
                for id, child_node in node.children.items():
                    # 
                    if dfs(child_node, word_id + 1):
                        return True
                else:    
                    return False
            else:
                node = node.children[word[word_id]]
                if dfs(node, word_id + 1):
                    return True
                else:
                    return False
            
        return dfs(node, 0)