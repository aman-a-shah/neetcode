import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        heapq.heapify(self.stream)
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

        if self.stream:
            return self.stream[0]
        else:
            return -1
