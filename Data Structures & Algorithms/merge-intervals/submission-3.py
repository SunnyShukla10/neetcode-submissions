class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] > res[-1][1]:
                res.append(curr)
            else:
                # have to merge 
                o_start, o_end = res[-1][0], res[-1][1] 
                c_start, c_end = curr[0], curr[1]

                res[-1] = [min(o_start, c_start), max(o_end, c_end)]

            print(res)
        return res