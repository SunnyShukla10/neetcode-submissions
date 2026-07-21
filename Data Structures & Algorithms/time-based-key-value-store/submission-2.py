class TimeMap:

    def __init__(self):
       self.d = {} # key : list of [value, timestamp] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value,timestamp])
        else:
            self.d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.d:
            return "" 

        pair_list = self.d[key]

        l, r = 0, len(pair_list) - 1
        res = ""
        while l <= r:
            m = (l+r) // 2
            if pair_list[m][1] > timestamp:
                r = m - 1
            else: 
                # the closest we have seen so far
                res = pair_list[m][0]
                l = m + 1
        return res
