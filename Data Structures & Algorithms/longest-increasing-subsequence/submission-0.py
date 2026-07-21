class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) 
        # O(n^2)
        for i in range(len(nums)-1, -1,-1):
            max_val = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
        return max(dp)
        