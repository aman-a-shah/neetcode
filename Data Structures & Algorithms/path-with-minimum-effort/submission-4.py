import heapq
from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # djikstra's, weights are the current max_diff on a path
        q = [(0,0,0)] # max_diff, i, j
        visited = set()

        while q:
            dist, i, j = heapq.heappop(q)
            if (i, j) in visited:
                continue

            visited.add((i, j))

            if (i, j) == (len(heights)-1, len(heights[0])-1):
                return dist

            if i > 0 and (i-1, j) not in visited:
                new_dist = max(dist, abs(heights[i][j]-heights[i-1][j]))
                heapq.heappush(q, (new_dist, i-1, j))
            if j > 0 and (i, j-1) not in visited:
                new_dist = max(dist, abs(heights[i][j]-heights[i][j-1]))
                heapq.heappush(q, (new_dist, i, j-1))
            if i < len(heights)-1 and (i+1, j) not in visited:
                new_dist = max(dist, abs(heights[i][j]-heights[i+1][j]))
                heapq.heappush(q, (new_dist, i+1, j))
            if j < len(heights[0])-1 and (i, j+1) not in visited:
                new_dist = max(dist, abs(heights[i][j]-heights[i][j+1]))
                heapq.heappush(q, (new_dist, i, j+1))
        
        return -1
        

