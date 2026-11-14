from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # k
        # nx2 rowC (above, below), mx2 colC (left, right)
        # rowC and colC contain int 1-k
        # create kxk grid with num 1-k each once and remaining 0

        # build graph + topo list
        def topo_ord(conditions):
            rank = [0 for _ in range(k+1)]
            graph = {i+1:[] for i in range(k)}
            for above, below in conditions:
                graph[above].append(below)
                rank[below] += 1
            
            res = []
            q = deque([node for node in graph if rank[node] == 0])
            while q:
                cur_rank_len = len(q)
                for i in range(cur_rank_len):
                    node = q.popleft()
                    res.append(node)
                    for nxt in graph[node]:
                        rank[nxt] -= 1
                        if rank[nxt] == 0:
                            q.append(nxt)
            return res

        r_res = topo_ord(rowConditions)
        c_res = topo_ord(colConditions)

        if len(r_res) != k or len(c_res) != k:
            return []

        # merge into grid
        grid = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if r_res[i] == c_res[j]:
                    grid[i][j] = r_res[i]
        return grid
