class TimeMap:

    def __init__(self):
        self.time_map: dict[str : list[str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map.get(key, [])
        res = ""
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l+r)//2
            if arr[m][0] <=timestamp:
                l = m + 1
                res = arr[m][1]
            else:
                r = m - 1
        
        return res
