from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # construct tree
        # height = max(height of neighbours)

        # 1. graph
        graph = {i:[] for i in range(n)}
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            graph[n1].append(n2)
            graph[n2].append(n1)

        # 2. go through tree from every leaf (1 edge), track max dist
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
            
        node_to_max_dist = {i:0 for i in range(n)}
        for leaf in leaves:
            # bfs
            visited = set()
            q = deque([(leaf, 1)])

            while q:
                node, dist = q.popleft()
                visited.add(node)
                node_to_max_dist[node] = max(node_to_max_dist[node], dist)

                for n in graph[node]:
                    if n not in visited:
                        q.append((n, dist+1))

        # 3. find min max-dist
        min_so_far = float('inf')

        for node in node_to_max_dist:
            min_so_far = min(min_so_far, node_to_max_dist[node])

        # 4. acc all root with min max-dist
        res = []
        for node in node_to_max_dist:
            if node_to_max_dist[node] == min_so_far:
                res.append(node)
            
        return res