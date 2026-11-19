class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # separated and sorted intervals
        # 1. find interval start
        start = newInterval[0]
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                start = min(start, intervals[i][0])
                break
        # 2. find interval end
        end = newInterval[1]
        for i in range(len(intervals)-1, -1, -1):
            if intervals[i][0] <= newInterval[1]:
                end = max(intervals[i][1], newInterval[1])
                break
        
        # return updated intervals
        res = []
        i = 0
        while i < len(intervals) and intervals[i][0] < start:
            res.append(intervals[i])
            i += 1
        res.append([start, end])
        while i < len(intervals) and intervals[i][1] <= end:
            i += 1
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res