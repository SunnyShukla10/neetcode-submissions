class TimeMap:

    def __init__(self):
       self.d = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = (value, timestamp)
        self.d[key].append(val)
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        res = ""
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            val, ts = arr[m]

            if ts <= timestamp:
                res = val
                l = m + 1            
            else:
                r = m - 1
        return res


