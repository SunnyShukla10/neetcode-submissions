class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for l in w: 
                count[ord(l) - ord('a')] += 1
            
            d[tuple(count)].append(w)

        return d.values()