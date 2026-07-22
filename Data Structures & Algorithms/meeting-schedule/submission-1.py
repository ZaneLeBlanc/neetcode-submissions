"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import attrgetter

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=attrgetter('start'))

        lastEnd = 0
        for i in intervals:
            if i.start < lastEnd:
                return False
            lastEnd = i.end
        return True

