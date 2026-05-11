class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        indegree = Counter({c: 0 for word in words for c in word})

        # build pairwise relationship for every adjacent words
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegree[d] += 1

                    break # no point going further
            else: # check if it gets here, we check if the second word is the prefix of the first word
                if len(second_word) < len(first_word):
                    return ""

            
        
        # do BFS, put all nodes with no indegree into a queue
        bfs_q = deque(c for c in indegree if indegree[c] == 0)
        # first put all the letters with no indegree into reachable
        

        proper_order = []
        while bfs_q:
            curr_val = bfs_q.popleft()
            proper_order.append(curr_val)
            # access the edges, and put them in the queue, and remove them
            curr_edges = adj_list[curr_val] # minus their indegree by 1, if it's 0, put it in the queue
            for edge in curr_edges:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    bfs_q.append(edge)

        if len(proper_order) < len(indegree):
            return ""
        
        return "".join(proper_order)