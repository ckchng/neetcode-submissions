class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree of n nodes has n-1 edges. This terminate immediately if the tree has too less or too many connectivity
        if len(edges) != n - 1:
            return False
        
        if len(edges) == 0 and n == 1:
            return True
        edge_hash = {}
        for edge in edges:
            if edge[0] in edge_hash:
                edge_hash[edge[0]].append(edge[1])
            else:
                edge_hash[edge[0]] = [edge[1]]
            
            if edge[1] in edge_hash:
                edge_hash[edge[1]].append(edge[0])
            else:
                edge_hash[edge[1]]= [edge[0]]

        # do dfs from any node, if it visits every nodes, it's a valid tree
        visited = set()
        def dfs(node_val):
            if node_val in visited:
                return
            
            visited.add(node_val)

            for neighbour in edge_hash[node_val]:
                dfs(neighbour)

        dfs(edge[0])
        return len(visited) == n