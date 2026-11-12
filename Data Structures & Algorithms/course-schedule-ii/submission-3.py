from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs_left = {crs:0 for crs in range(numCourses)}
        prereq_to_crs = {crs:[] for crs in range(numCourses)}

        for crs, prereq in prerequisites:
            prereqs_left[crs] += 1
            prereq_to_crs[prereq].append(crs)
        
        q = deque([crs for crs in prereqs_left if prereqs_left[crs] == 0])
        res = []

        while q: 
            crs = q.popleft()
            res.append(crs)

            for n in prereq_to_crs[crs]:
                prereqs_left[n] -= 1
                if prereqs_left[n] == 0:
                    q.append(n)
        
        if all(prereqs_left[crs] == 0 for crs in prereqs_left):
            return res
        else:
            return []
        