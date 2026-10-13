import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            dist = abs(x-num)
            heapq.heappush(heap, (-dist, -num))

            if len(heap) > k:
                heapq.heappop(heap)

        acc = sorted([-(x[1]) for x in heap])
        return acc

        