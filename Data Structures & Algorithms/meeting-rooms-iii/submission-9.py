class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # n rooms 0 - n-1
        # meetings[i] from [start, end)
        # all starts are unique

        meetings_count = [0] * n
        meetings.sort()
        
        heap = [] # (end_time, room_index)
        available = list(range(n))
        heapq.heapify(available)


        for start, end in meetings:
            while heap and heap[0][0] <= start:
                _, room = heapq.heappop(heap)
                heapq.heappush(available, room)

            if len(heap) < n:
                room = heapq.heappop(available)
                heapq.heappush(heap, (end, room))
                meetings_count[room] += 1
            else:
                time, i = heapq.heappop(heap)
                duration = end - start
                heapq.heappush(heap, (time + duration, i))
                meetings_count[i] += 1
            
        # find max meetings room
        max_meets, idx = 0, 0
        for i in range(n):
            if meetings_count[i] > max_meets:
                max_meets = meetings_count[i]
                idx = i
        return idx
    
        # [(20, 0), (10, 1), ]
            