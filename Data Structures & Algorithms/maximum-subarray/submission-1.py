class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] + curr_sum >= nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            res = max(res, curr_sum)
            print(res, " ", curr_sum)
        return res