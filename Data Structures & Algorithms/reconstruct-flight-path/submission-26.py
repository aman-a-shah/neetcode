from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build graph (tickets = edges)
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
            

        for node in graph:
            graph[node].sort(reverse=True)

        path = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())   # pop() = smallest remaining edge
            path.append(node)            # post-order append

        dfs("JFK")
        return path[::-1]  