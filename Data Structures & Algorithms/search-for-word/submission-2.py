class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # keep a hash table of the explored (r_id, c_id)

        # explore the three options, if the r_id, c_id is not in the hash_table, 
        # check if the matched the next character, if they do, keep going and add the r_id and c_id into the hash table
        # if none of the available options matches, pop r_id and c_id from the hash table, go back up the stack

        if Counter(word) - Counter(c for row in board for c in row):
            return False
        options = [[1, 0], [0, 1], [-1, 0], [0, -1]] # only these four options
        visited = set()
        def backtrack(r_id, c_id, word_idx):

            
            if word_idx == len(word):
                return True
            if r_id >= len(board) or c_id >= len(board[0]) or r_id < 0 or c_id < 0:
                return False
            if (r_id, c_id) in visited:
                return False
            if board[r_id][c_id] != word[word_idx]:
                return False
            
            # if none of the termination conditions are met, we keep going with word_idx
            # and add the row and column id
            visited.add((r_id, c_id))
            
            for option in options:    
                curr_r = r_id + option[0]
                curr_c = c_id + option[1]
            
                if backtrack(curr_r, curr_c, word_idx + 1):
                    return True
                
            visited.remove((r_id, c_id))
        
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True

        return False