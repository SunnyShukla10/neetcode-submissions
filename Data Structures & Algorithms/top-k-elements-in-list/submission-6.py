class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # list where idx corresponds to occurences and the value refers to the number

        # 1,2,2,3,3,3 --> [0,1,2,3,0,0]
        # iterate from the back of the list and find the k most occurences that way
        d = {} # counts occurences

        for n in nums: 
            d[n] = 1 + d.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for val, occurences in d.items():
            freq[occurences].append(val)
        ret = []
        for i in range(len(freq) - 1, -1, -1):
            for item in freq[i]:
                if item != None:
                    ret.append(item)
                if len(ret) == k:
                    return ret