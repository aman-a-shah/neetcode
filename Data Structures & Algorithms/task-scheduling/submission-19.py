from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        let_freq = Counter(tasks)
        maxHeap = [-cnt for cnt in let_freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            if maxHeap:
                freq = -heapq.heappop(maxHeap)
                if freq > 1:
                    q.append((-(freq-1), time+n))
            
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
            time += 1

        return time
