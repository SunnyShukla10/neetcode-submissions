class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        res = float('inf')
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            length = 0
            while sum >= target:
                res = min(res, r-l+1)
                sum -= nums[l]
                l += 1

        return 0 if res == float('inf') else res
         