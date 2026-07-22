class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums: # 1
            freq[n] = freq.get(n, 0) + 1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_freq.keys())
        return sorted_keys[0:k]