class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0) 
        
        freq = [[] for _ in range(len(nums)+1)]

        for num, cnt in d.items():
            freq[cnt].append(num)
        
        res = [] 
        for i in range(len(freq)- 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
       