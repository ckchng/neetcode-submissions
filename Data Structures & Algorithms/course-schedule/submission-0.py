class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = {}
        for pre in prerequisites:
            course = pre[0]                
            p = pre[1]

            indegree[course] += 1

            if p in adj_list:   
                adj_list[p].append(course)
            else:
                adj_list[p] = [course]

        q = deque()
        for id, value in enumerate(indegree):
            if value == 0:
                q.append(id)
        

        while q:
            curr_course = q.popleft()
            # extract the courses unlocked
            unlock_courses = adj_list.get(curr_course, [])
            # minus indegree
            for u_c in unlock_courses:
                indegree[u_c] -= 1
                if indegree[u_c] == 0:
                    q.append(u_c)

        # if there are still course with indegree > 0:
        if sum(indegree) > 0:
            return False
        
        return True