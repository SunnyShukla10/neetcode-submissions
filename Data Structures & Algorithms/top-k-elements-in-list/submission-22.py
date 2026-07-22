class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count: 'Counter' = Counter(nums)

        freq_list: List[List[int]] = [[] for i in range(len(nums) + 1)]
        
        for val, freq in count.items():
            freq_list[freq].append(val)
        
        res: List[int] = []
        for i in range(len(freq_list)-1, -1, -1):
            for val in freq_list[i]:
                res.append(val)

                if len(res) == k:
                    return res
                
        
        return -1