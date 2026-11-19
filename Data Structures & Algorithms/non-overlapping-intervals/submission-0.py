class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # create adjacency graph of overlapping
        # remove interval with most neighbours

        intervals.sort()                      
        removed = 0
        
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:              # overlap: one of the two must go
                removed += 1
                prev_end = min(prev_end, end) # keep whichever ends sooner
            else:
                prev_end = end                # no overlap, move on
        
        return removed