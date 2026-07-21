class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            d1[s[i]] = 1 + d1.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)
        
        return d1 == d2
