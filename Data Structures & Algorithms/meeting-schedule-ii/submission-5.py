"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals sorted by start
        intervals.sort(key=lambda x:x.start)

        # add into heap by start time
        # remove from heap by end time
        # return max size of heap

        heap = []
        res = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            if heap and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)
            res = max(res, len(heap))
        
        return res


