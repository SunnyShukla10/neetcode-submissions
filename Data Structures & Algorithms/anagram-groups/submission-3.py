class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array --> [0, ... , 25] 0 = a, 25 = z
        
        # defaultdict(list) --> creates a list as the value of each key
        d = defaultdict(list) #  alphabet_array: [{words pertaining to this}]

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1

            d[tuple(count)].append(word)
        
        return d.values()