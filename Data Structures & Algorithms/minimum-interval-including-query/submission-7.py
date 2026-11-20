import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals and ints in queries
        # for each query, return shortest interval length that holds that query

        intervals.sort()
        query_res = {}
        query_sort = sorted(queries)
        
        heap = []

        i = 0

        for q in query_sort:
            # want all intervals start <= q, end >= q
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1])) # (length, end)
                i += 1
            
            # remove intervals that end < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            query_res[q] = heap[0][0] if heap else -1
        
        return [query_res[q] for q in queries]