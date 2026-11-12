class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges)+1)]

        def find_parent(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb:
                return [a, b]
            parent[pb] = parent[pa]            

        
