from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. graph
        graph = defaultdict(list) # str:list[tuple[str, weight]]
        for i, equation in enumerate(equations):
            n1, n2 = equation[0], equation[1]
            
            graph[n1].append((n2, values[i]))
            graph[n2].append((n1, 1/values[i]))
            
        # 2. dfs
        def dfs(node, visited, acc):
            if node not in graph:
                return None
            if node == end:
                return acc
            
            for n, weight in graph[node]:
                if n in visited:
                    continue

                visited.add(n)
                x = dfs(n, visited, acc*weight)
                visited.remove(n)
                if x:
                    return x
            
            return None

        # 3. traverse each query + append to result
        res = []
        for query in queries:
            start = query[0]
            end = query[1]

            x = dfs(start, set(), 1)
            if x:
                res.append(x)
            else:
                res.append(-1)

        return res