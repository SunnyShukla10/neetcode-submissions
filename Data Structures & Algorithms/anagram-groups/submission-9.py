class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for l in w:
                count[ord('a') - ord(l)] += 1
            d[tuple(count)].append(w)
        
        res = []
        for val in d.values():
            res.append(val)

        return res 