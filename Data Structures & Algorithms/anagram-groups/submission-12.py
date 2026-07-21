class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            # array filled with 0s for the length of the alphabet
            arr = [0] * 26
            for l in word:
                arr[ord('a') - ord(l)] += 1
            d[tuple(arr)].append(word)
        
        return list(d.values())

