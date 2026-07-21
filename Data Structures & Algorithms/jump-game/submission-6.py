class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l,r = 0, 0

        while r < len(nums) - 1:

            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
                
            if farthest <= r:
                return False
            
            l = r+1
            r = farthest

        return True