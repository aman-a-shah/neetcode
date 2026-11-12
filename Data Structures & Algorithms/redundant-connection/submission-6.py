class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # no cycles, fully connected, n node, n-1 edges
        """
        brute force: go through edges backwards, check connected, check cycels
            - remove
            - bfs out and see if cycle OR check connected (go thorugh all nodes and see if eliminating edge create)
        """

        # graph
        graph = {n+1:[] for n in range(len(edges))}
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            graph[n1].append(n2)
            graph[n2].append(n1)

        removable = set()
        switch = True
        while switch:
            switch = False

            for node in graph:
                if node in removable:
                    continue
                count = 0
                for n in graph[node]:
                    if n not in removable:
                        count += 1
                if count == 1:
                    removable.add(node)
                    switch = True

        # check for first edge not in single_edges
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] not in removable and edges[i][1] not in removable:
                return edges[i]

