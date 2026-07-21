class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        for i, s in enumerate(s):
            if s not in intervals:
                intervals[s] = [i,i]
            else:
                intervals[s][1] = i

        # merge the intervals
        res = []
        for letter, (start, end) in intervals.items():
            if len(res) == 0:
                res.append([start,end])
                continue
            
            if start < res[-1][1]: # merge
                res[-1] = [res[-1][0], max(res[-1][1], end)]
            else:
                res.append([start,end])


        
        return [e - s + 1 for s, e in res] 