from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # 1. graph
        graph = {i:[] for i in range(n)}
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        degree = {i: len(graph[i]) for i in range(n)}

        # 2. leaves
        q = deque()
        for node in graph:
            if len(graph[node]) <= 1:
                q.append(node)
        
        # 3. peel away one by one
        remaining = n
        while remaining > 2:
            for _ in range(len(q)):
                node = q.popleft()
                remaining -= 1
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        # whatever is left in the queue are the centers
        return list(q)