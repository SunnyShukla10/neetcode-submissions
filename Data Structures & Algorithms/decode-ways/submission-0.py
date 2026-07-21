class Solution:
    def numDecodings(self, s: str) -> int:
        # make sure it doesn't start with 0
        # make sure its between 1-26

        dp = {len(s): 1}

        def dfs(i):
            # edge cases
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            
            res = dfs(i+1)

            if (i+1 < len(s)) and int(s[i:i+2]) in range(1,27):
                res += dfs(i+2)

            dp[i] = res
            return res 

        return dfs(0) 