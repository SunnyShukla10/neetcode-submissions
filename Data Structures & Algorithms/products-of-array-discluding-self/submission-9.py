class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prev = 1
        for i in range(len(nums)):
            res.append(prev)
            prev *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res