class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # list where idx corresponds to occurences and the value refers to the number

        # 1,2,2,3,3,3 --> [0,1,2,3,0,0]
        # iterate from the back of the list and find the k most occurences that way

        l = [[] for i in range(len(nums) + 1)]

        d = {} # value : num occurences
        x = 0
        output_list = []
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        for val, occurences in d.items():
            l[occurences].append(val)

        for i in range(len(l) - 1, -1, -1):
            for num in l[i]:
                output_list.append(num)
                if len(output_list) == k:
                    return output_list