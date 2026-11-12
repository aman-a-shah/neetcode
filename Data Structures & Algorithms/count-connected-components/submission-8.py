from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct graph
        # count nodes with no edges
        # return n-(that val)

        graph = {i:[] for i in range(n)}
        for i in range(len(edges)):
            n1, n2 = edges[i][0], edges[i][1]
            graph[n1].append(n2)
            graph[n2].append(n1)

        # bfs
        def bfs(node):
            q = deque([node])
            nonlocal visited

            while q:
                nxt = q.popleft()
                visited.add(nxt)
                for n in graph[nxt]:
                    if n not in visited:
                        q.append(n)

        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                count += 1
                bfs(node)
        
        return count
