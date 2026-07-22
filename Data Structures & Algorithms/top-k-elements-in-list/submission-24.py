class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # freq map
        freq = Counter(nums)
        
        max_val = max(freq.values())
        arr = [[] for i in range(max_val+1)]

        for key, val in freq.items():
            arr[val].append(key)
        
        res = []
        for i in range(len(arr)-1, -1, -1):
            if not arr[i]:
                continue
            
            for val in arr[i]:
                res.append(val)
                if len(res) == k:
                    return res
    
        return -1