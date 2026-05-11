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
        # if it's not '.' search as usual

        node = self.root

        def dfs(node, word_idx):
            # termination condition is
            if word_idx == len(word) and node.is_end:
                return True
            if word_idx == len(word) and not (node.is_end):
                return False
            if word[word_idx] != '.' and word[word_idx] not in node.children:
                return False
            if node.children is None:
                return False

            # iterate through the children
            if word[word_idx] == '.':
                for child in node.children:
                    if dfs(node.children[child], word_idx+1):
                        return True
                return False
                        
            else:
                return dfs(node.children[word[word_idx]], word_idx+1)


        return dfs(node, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)