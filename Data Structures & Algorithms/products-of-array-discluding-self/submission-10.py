class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # arr = [48, 24, 12, 8] post = 1
        arr = []

        pre = 1
        for i in range(len(nums)):
            arr.append(pre)
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1,-1):
            arr[i] *= post
            post *= nums[i]

        return arr