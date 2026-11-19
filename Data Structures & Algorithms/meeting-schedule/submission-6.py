"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # turn to list
        intervals_list = [[interval.start, interval.end] for interval in intervals]
        #sort list
        intervals_list.sort()

        if not intervals:
            return True
        prev_end = intervals_list[0][1]
        for start, end in intervals_list[1:]:
            if start < prev_end:
                return False
            prev_end = end
        return True