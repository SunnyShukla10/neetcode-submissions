class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # list where idx corresponds to occurences and the value refers to the number

        # 1,2,2,3,3,3 --> [0,1,2,3,0,0]
        # iterate from the back of the list and find the k most occurences that way
        d = {} # counts occurences

        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        count = [[] for i in range(len(nums) + 1)]
        for v, o in d.items():
            count[o].append(v)
        
        res = []
        for i in range(len(nums), -1 ,-1):
            for item in count[i]:
                if item != None:
                    res.append(item)

            if len(res) == k:
                return res    
            