class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # stores key : [(val, ts), (val2, ts) ... ] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.d:
            return ""
        
        pair_list = self.d[key]
        
        l,r = 0, len(pair_list) - 1

        while l <= r:
            m = (r + l) // 2
            if pair_list[m][1] <= timestamp:
                # we got a possible result 
                res = pair_list[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res


