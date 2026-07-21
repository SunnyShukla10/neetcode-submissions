class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set
        seen = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            # if the letter wasn't in the set already
            seen.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len