class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start from all locations
        # keep going with dfs until you cant find any '1'
        # return 1 + 
        
        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if grid[r][c] == '0':
                return
            
            options = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            grid[r][c] = '0'
            for option in options:
                
                dfs(r + option[0], c + option[1])

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_islands += 1
        return num_islands