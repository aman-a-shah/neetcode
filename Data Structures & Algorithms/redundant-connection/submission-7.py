class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))   # each node starts as its own group

        def find(x):                            # find the group's representative
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:                        # already connected -> this edge makes a cycle
                return [a, b]
            parent[rb] = ra                     # merge the two groups