class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        group = list(range(len(edges) + 1))   # every node starts in its own group

        for a, b in edges:
            if group[a] == group[b]:          # already connected -> this edge makes a cycle
                return [a, b]

            old, new = group[b], group[a]     # otherwise merge b's group into a's
            for i in range(len(group)):
                if group[i] == old:
                    group[i] = new