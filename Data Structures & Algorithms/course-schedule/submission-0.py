from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_class = {cls:[] for cls in range(numCourses)}
        prereqs_left = {cls:0 for cls in range(numCourses)}

        for cls, prereq in prerequisites:
            prereq_to_class[prereq].append(cls)
            prereqs_left[cls] += 1
        
        q = deque([cls for cls in prereqs_left if prereqs_left[cls] == 0])

        while q:
            cls = q.popleft()
            for n in prereq_to_class[cls]:
                prereqs_left[n] -= 1
                if prereqs_left[n] == 0:
                    q.append(n)
        
        return all([prereqs_left[cls] == 0 for cls in prereqs_left])



