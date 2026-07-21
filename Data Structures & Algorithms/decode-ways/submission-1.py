class Solution:
    def numDecodings(self, s: str) -> int:
        
        # we iterate over each letter of string, we decide either to choose 1 or 2 digits (not more or less) and solve the subproblem of i+1 or i+2
        memo = {len(s): 1} # maps the idx and number of decodings for that idx

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)

            if (i+1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)

            memo[i] = res
            return res        

        return dfs(0)

