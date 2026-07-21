class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # only evens will work
        if sum(nums) % 2 != 0:
            return False
        
        half = sum(nums) / 2
        memo = {}
        def dfs(i, val):
            if val == 0:
                return True    

            if i >= len(nums):
                return False
            
            if val in memo:
                return memo[val]

            # choose curr val
            res = dfs(i+1, val - nums[i]) or dfs(i+1, val)
            memo[val] = res
            return res

        return dfs(0, half) 
