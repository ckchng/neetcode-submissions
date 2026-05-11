class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if len(heights) == 0 or len(heights[0]) == 0:
            return []
        # gotta initialise with all the (r, c) near the edge, put them as visited
        pacific_tiles = deque()
        atlantic_tiles = deque()

        for c in range(len(heights[0])):
            pacific_tiles.append((0, c))
        for r in range(len(heights)):
            pacific_tiles.append((r, 0))
        
        for c in range(len(heights[0])):
            atlantic_tiles.append((len(heights)-1, c))
        for r in range(len(heights)):
            atlantic_tiles.append((r, len(heights[0])-1))

        options = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        def bfs(queue):
            reachable = set()
            while queue:
                rc = queue.popleft()
                reachable.add(rc)

                # then check the options
                for option in options:
                    curr_r = rc[0] + option[0]
                    curr_c = rc[1] + option[1]

                    if (curr_r, curr_c) in reachable:
                        continue
                    
                    if curr_r >= len(heights) or curr_c >= len(heights[0]) or curr_r < 0 or curr_c < 0:
                        continue

                    # if it's reachable, we add to queue
                    if heights[curr_r][curr_c] >= heights[rc[0]][rc[1]]:
                        queue.append((curr_r, curr_c))
            
            return reachable
        
        #Check both 
        pacific_reachable = bfs(pacific_tiles)
        atl_reachable = bfs(atlantic_tiles)

        # intersect
        both_reachable = pacific_reachable.intersection(atl_reachable)
        
        return list(both_reachable)