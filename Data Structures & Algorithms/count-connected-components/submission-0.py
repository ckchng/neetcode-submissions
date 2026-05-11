class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # put all nodes in a set
        graph = collections.defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        count = 0  
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbour in graph[node]:
                dfs(neighbour)

            return

        for i in range(n):
            if i not in visited: 
                dfs(i)
                count+=1
            
        return count