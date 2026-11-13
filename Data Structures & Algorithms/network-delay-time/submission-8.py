import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # construct a graph using times as edges
        graph = {i+1:[] for i in range(n)}
        for time in times:
            n1, n2, wgt = time[0], time[1], time[2]
            graph[n1].append((n2, wgt))

        # bfs out until all nodes reached
        q = [(0, k)]
        visited = set()
        while q:
            wgt, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return wgt

            for nxt, nxt_wgt in graph[node]:
                heapq.heappush(q, (nxt_wgt+wgt, nxt))

        return -1