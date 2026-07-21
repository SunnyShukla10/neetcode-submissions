class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have each key value be 
        # char array count : list of words
        d = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord('a')] += 1    
            d[tuple(count)].append(word)
        
        return list(d.values())