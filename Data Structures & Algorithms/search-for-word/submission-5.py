class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # same as before, we do DFS with backtracking, each cell can be followed by four options, 
        # this time, it's 2D, it's a grid, so, we need a visited to keep track of the cells that we have visited before
        # remember the append, recurse, pop
        
        # if the unique word in board is shorter than word, return false
        count = Counter(board[r][c] for r in range(len(board)) for c in range(len(board[0])))
        for char, needed in Counter(word).items():
            if count[char] < needed:
                return False
        
        visited = set()
        options = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs_backtrack(r, c, curr_word_id):
            if curr_word_id == len(word):
                return True

            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return False
            
            if (r, c) in visited:
                return False
            
            if board[r][c] != word[curr_word_id]:
                return False
            
            visited.add((r, c))
            
            for option in options:
                curr_r = r + option[0]
                curr_c = c + option[1]

                if dfs_backtrack(curr_r, curr_c, curr_word_id+1):
                    return True

            visited.remove((r, c))

            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs_backtrack(r, c, 0):
                        return True
                    
        return False