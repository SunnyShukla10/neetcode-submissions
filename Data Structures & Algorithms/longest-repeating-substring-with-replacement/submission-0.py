class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res = 0
        d = {} # Letter in alphabet : count
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            
            if (r-l+1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r-l+1) 
        return res