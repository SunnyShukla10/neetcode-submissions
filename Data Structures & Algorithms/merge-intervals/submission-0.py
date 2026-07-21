class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])

        res: List[List[int]] = []
        to_merge: List[int] = intervals[0] 

        for i in range(1, len(intervals)):
            if to_merge[1] < intervals[i][0]:
                res.append(to_merge)
                to_merge = intervals[i]
            else:
                # overlapping
                to_merge = [min(to_merge[0], intervals[i][0]), max(to_merge[1], intervals[i][1])]
                print(to_merge)
        res.append(to_merge)
        return res    
        
            # overlap
            # curr iterval after to_merge or before to_merge
            