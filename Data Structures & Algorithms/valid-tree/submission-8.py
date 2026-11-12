from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        # construct tree
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # check for cycles
        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for i in graph[node]:
                q.append(i)

        return len(visited) == n