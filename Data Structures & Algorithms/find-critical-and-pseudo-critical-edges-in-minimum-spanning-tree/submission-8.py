class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # want to build MST
        # sort edges by weight
        # union find until n-1 edges

        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [0 for _ in range(n)]
            
            def find(self, x):
                p = self.parent[x]
                while x != p:
                    p = self.parent[p]
                    x = self.parent[x]
                return x
            
            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return False

                if self.rank[py] > self.rank[px]:
                    self.parent[px] = py
                elif self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                else:
                    self.parent[px] = py
                    self.rank[py] += 1
                
                return True
                
        def mst(edges, start = None):
            x = sorted(edges, key=lambda x: x[2])
            if start:
                x = start+x

            uf = UnionFind(n)
            total, count = 0, 0

            for i in range(len(x)):
                a, b, weight = x[i]
                if uf.find(a) == uf.find(b):
                    continue
                uf.union(a, b)
                total += weight
                count += 1
                if count == n-1:
                    return total
            
            return -1
            raise ValueError('no mst possible with edges')
        
        # base
        base = mst(edges)
        crit = []
        pseudo_crit = []

        # for each edge:
        #   if no build without edge (critical) 
        #   else if possible with edge, pseudo-critical
        for i in range(len(edges)):
            wgt = mst(edges[:i]+edges[i+1:])
            if wgt != base:
                crit.append(i)
                continue
            
            wgt = mst(edges[:i]+edges[i+1:], [edges[i]])
            if wgt == base:
                pseudo_crit.append(i)
                continue
            
        return [crit, pseudo_crit]

            

