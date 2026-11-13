import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i + 1: [] for i in range(n)}
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]                 # (cumulative_time, node)
        visited = set()

        while q:
            dist, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return dist

            for nxt, w in graph[node]:
                if nxt not in visited:
                    heapq.heappush(q, (dist + w, nxt))

        return -1