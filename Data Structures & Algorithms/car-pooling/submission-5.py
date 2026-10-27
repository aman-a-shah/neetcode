from collections import deque
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_pass = 0
        cur_pos = 0

        dest = [] # pos, num_pass
        trips.sort(key=lambda x:x[1])
        trips = deque(trips)

        while trips:
            while dest and cur_pos == dest[0][0]:
                drop_of = heapq.heappop(dest)
                cur_pass -= drop_of[1]

            if cur_pos == trips[0][1]:
                trip = trips.popleft()
                
                cur_pass += trip[0]
                if cur_pass > capacity:
                    return False
                heapq.heappush(dest, [trip[2], trip[0]])

            if dest and trips:
                cur_pos = min(trips[0][1], dest[0][0])
            elif dest:
                cur_pos = dest[0][0]
            elif trips:
                cur_pos = trips[0][1]
                
        return True

