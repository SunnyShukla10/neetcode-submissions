class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def backtrack(i,j):
            
            if j >= len(s):
                if i == j:
                    res.append(subset.copy())
                return
            
            if self.isPalindrome(s,i,j):
                subset.append(s[i:j+1])
                backtrack(j+1, j+1)
                subset.pop()
            
            backtrack(i, j+1)


        backtrack(0,0)
        return res
    
    def isPalindrome(self, s:str, i: int, j:int) -> bool:
        l, r = i, j

        while l < r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True
