class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            max_len = max(r-l + 1, max_len)
            

        return max_len