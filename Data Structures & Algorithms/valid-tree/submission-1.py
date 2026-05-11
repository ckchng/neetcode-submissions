class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # the key here is that a valid tree of n nodes has exactly n-1 edges 
        if len(edges) != n-1:
            return False
        
        if len(edges) == 0 and n == 1:
            return True
        
        # first hash the edges, easier for access later
        edge_hash = {}
        for edge in edges:
            if edge[0] in edge_hash:
                edge_hash[edge[0]].append(edge[1])
            else:
                edge_hash[edge[0]] = [edge[1]]
            
            if edge[1] in edge_hash:
                edge_hash[edge[1]].append(edge[0])
            else:
                edge_hash[edge[1]] = [edge[0]]
            
        # do dfs, if it visits every single node, it's a valid tree\
        visited = set()
        def dfs(node):
            # take a node, check all of its neighbour
            # if visited, return,
            # if not, keep going
            # return when visited == n
            if node in visited:
                return
            
            if len(visited) == n:
                return 
            
            visited.add(node)

            for neighbour in edge_hash[node]:
                dfs(neighbour)

        dfs(edges[0][0])
        return len(visited) == n