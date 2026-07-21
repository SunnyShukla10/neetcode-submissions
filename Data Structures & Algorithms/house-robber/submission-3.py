class Solution:
    def rob(self, nums: List[int]) -> int:

        # so we are building each idx setting that idx by taking the max of prev element or curr elem + idx-2 elem 
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        one = nums[0]
        two = max(one, nums[1]) 
        
        for i in range(2, len(nums)):
            temp = max(one + nums[i], two)
            one = two
            two = temp
        
        return two