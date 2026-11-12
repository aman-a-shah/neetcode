from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # construct tree
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # check for cycles
        visited = set()
        q = deque([(0, None)])

        while q:
            node, prev = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for i in graph[node]:
                if i != prev:
                    q.append((i, node))

        if len(visited) == n:
            return True
        else:
            return False
