class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_tab = {}
        col_tab = {}
        square_tab = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                curr_num = board[i][j]
                if curr_num != '.':
                    if i not in row_tab:
                        row_tab[i] = []
                    
                    if j not in col_tab:
                        col_tab[j] = []
                    
                    curr_row_col = tuple([i//3, j//3])
                    if curr_row_col not in square_tab:
                        square_tab[curr_row_col] = []

                    if curr_num not in row_tab[i]:
                        row_tab[i].append(curr_num)
                    else:
                        return False
                    
                    if curr_num not in col_tab[j]:
                        col_tab[j].append(curr_num)
                    else:
                        return False
                    
                    if curr_num not in square_tab[curr_row_col]:
                        square_tab[curr_row_col].append(curr_num)
                    else:
                        return False
        return True