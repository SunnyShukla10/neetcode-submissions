class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, len(chars))
        return max_len
        