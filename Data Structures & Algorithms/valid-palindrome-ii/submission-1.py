class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        deleted = False

        while l < r:
            if s[l] != s[r]:
                return (self.isPalindrome(l + 1,r,s) or self.isPalindrome(l,r-1,s))
                
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNumeric(self, l):
        return (
            (ord("A") <= ord(l) <= ord("Z")) or 
            (ord("a") <= ord(l) <= ord("z")) or 
            (ord("0") <= ord(l) <= ord("9"))
        )
        
    def isPalindrome(self, l, r, s):
        
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
                
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True