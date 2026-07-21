class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            d[i] = pre
            pre *= nums[i]
        print(d)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            d[i] *= post
            post *= nums[i]
        
        return d