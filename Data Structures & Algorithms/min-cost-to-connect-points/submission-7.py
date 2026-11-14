from collections import defaultdict, deque
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # construct graph, all nodes to all others, sorted by manhattan distance
        def manhattan_dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                dist = manhattan_dist(points[i], points[j])
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        # pick cheapest connection
        visited = {0}
        cost = 0
        heap = []
        for dist, n in graph[0]:
            heapq.heappush(heap, (dist, n))

        while len(visited) < len(graph):
            dist, n = heapq.heappop(heap)
            if n in visited:
                continue
            visited.add(n)
            cost += dist
            for dst, nxt in graph[n]:
                if nxt not in visited:
                    heapq.heappush(heap, (dst, nxt))
        
        return cost