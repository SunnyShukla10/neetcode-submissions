class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array --> [0, ... , 25] 0 = a, 25 = z
        
        # defaultdict(list) --> creates a list as the value of each key
        d = defaultdict(list) #  alphabet_array: [{words pertaining to this}]
        
        # for each word create an array representing the letters of alphabet
        for word in strs:
            alpha = [0] * 26
            for l in word:
                print(ord(l) - ord('a'))
                alpha[ord(l) - ord('a')] += 1
            d[tuple(alpha)].append(word)
        return d.values()
        # loop over each word and fill the count to the array 
        # add this to a dictionary
        
        # return the values of the dictionary