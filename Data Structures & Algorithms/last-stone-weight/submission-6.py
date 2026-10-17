import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap:
            if len(heap) == 1:
                return -heap[0]

            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            
            diff = stone1 - stone2
            if diff > 0:
                heapq.heappush(heap, -diff)
        
        return 0