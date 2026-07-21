class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in d.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res

        return []