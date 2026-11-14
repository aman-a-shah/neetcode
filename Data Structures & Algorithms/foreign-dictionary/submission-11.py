from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # graph + rank
        graph = {c: [] for w in words for c in w}
        let_to_rank = {c:0 for c in graph}
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] == words[i+1][j]:
                    continue
                graph[words[i][j]].append(words[i+1][j])
                let_to_rank[words[i+1][j]] += 1
                break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ''

        # toposort str
        q = deque()
        for node in graph.keys():
            if let_to_rank[node] == 0:
                q.append(node)
        
        res = ''
        visited = set()
        while q:
            let = q.popleft()
            
            visited.add(let)
            res += let
            for nxt in graph[let]:
                let_to_rank[nxt] -= 1
                if let_to_rank[nxt] == 0:
                    q.append(nxt)
        
        if len(res) == len(graph):
            return res
        return ''

