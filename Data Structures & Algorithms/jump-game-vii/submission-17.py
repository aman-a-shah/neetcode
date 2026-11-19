from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # start at i = 0
        # can jump from i to j if s[j] == '0' and j inclusively inside min/max jump


        # recursion depth exceeded
        if s[-1] != '0':
            return False

        q = deque([0])
        visited = set()
        furthest = 0

        while q:
            i = q.popleft()
            if i == len(s)-1:
                return True
            if i in visited:
                continue
            visited.add(i)

            for j in range(max(i+minJump, furthest+1), min(i+maxJump+1, len(s))):
                if s[j] == '0':
                    q.append(j)
            furthest = maxJump+i

        return False