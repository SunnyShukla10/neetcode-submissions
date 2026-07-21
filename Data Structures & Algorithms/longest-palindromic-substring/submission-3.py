class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStartIdx = 0
        resLength = 0
        for i in range(len(s)):
            # odd
            l,r = i, i            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLength:
                    resStartIdx = l
                    resLength = r-l+1

                l -= 1
                r += 1
            
           

            # even case
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLength:
                    resStartIdx = l
                    resLength = r-l+1

                l -= 1
                r += 1
            

        return s[resStartIdx: resStartIdx + resLength]