class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # -4, -1, -1, 0, 1, 2
        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            
            l,r = i+1, len(nums) - 1
            
            while l < r:
                threesum = val + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res 