class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by s time
        intervals.sort(key=lambda x:x[1])
        
        prev: List[int] = intervals[0]
        res: int = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                res += 1
            else:
                prev = curr
        
        return res
