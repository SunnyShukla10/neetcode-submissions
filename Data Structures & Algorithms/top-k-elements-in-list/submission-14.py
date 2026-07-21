class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)] 
        for v, f in d.items():
            freq[f].append(v)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            if freq[i] != None:
                for val in freq[i]:
                    res.append(val)
                    
                    if len(res) == k:
                        return res