class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # list where idx corresponds to occurences and the value refers to the number

        # 1,2,2,3,3,3 --> [0,1,2,3,0,0]
        # iterate from the back of the list and find the k most occurences that way
        d = {}
        for val in nums:
            d[val] = 1 + d.get(val, 0)
        
        freq = [[] for i in range(len(nums) + 1)] 
        for v, o in d.items():
            freq[o].append(v)
    
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != None:
                for val in freq[i]:
                    res.append(val)
                    if len(res) == k:
                        return res
                        

