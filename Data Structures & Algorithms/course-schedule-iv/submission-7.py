from copy import deepcopy
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # make graph
        graph = {n:[] for n in range(numCourses)}
        for prereq, crs in prerequisites:
            graph[prereq].append(crs)
        
        # bfs + cache
        answer = [False] * len(queries)
        prereq_to_crs = {}
        
        for i, query in enumerate(queries):
            prereq, crs = query[0], query[1]
            if prereq in prereq_to_crs:
                answer[i] = crs in prereq_to_crs[prereq]
                continue

            q = deque([prereq])
            visited = set()
            while q:
                nxt = q.popleft()
                for n in graph[nxt]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
            prereq_to_crs[prereq] = visited
            answer[i] = crs in visited

        return answer
            
                

