class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # construct weighted graph
        graph = {i:[] for i in range(n)}
        for start, end, price in flights:
            graph[start].append((price, end))

        # djikstra's
        q = []; heapq.heappush(q, (0, 0, src)) # price, stops, node
        best = {}

        while q:
            price, stops, node = heapq.heappop(q)
            if node == dst:
                return price
            if stops > k:
                continue
            if (node, stops) in best and best[(node, stops)] <= price:
                continue
            best[(node, stops)] = price
            
            for nxt_price, nxt in graph[node]:
                heapq.heappush(q, (price+nxt_price, stops+1, nxt))
        
        return -1