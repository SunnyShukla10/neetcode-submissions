"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        
        rooms = []
        res = 1
        heapq.heappush(rooms, intervals[0].end)
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if rooms[0] > curr.start: # overlap
                heapq.heappush(rooms, curr.end)
                res += 1
            else:
                prevEnd = heapq.heappop(rooms)
                heapq.heappush(rooms, max(prevEnd, curr.end))

        return res    
