class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build edge_hash
        # start from any node, do dfs
        # everytime a node is visited, put it in, 
        # at the end of dfs, increase counter, 
        # instead of doing deletion, just check if the node is visited, skip if processed
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for con_node in graph[node]:
                dfs(con_node)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count