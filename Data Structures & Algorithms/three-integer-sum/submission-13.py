class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums
        nums.sort() # or nums = sorted(nums)
        res = []
        # iterate over each number
        for i in range(len(nums) - 1):
     
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
          
            l,r = i + 1, len(nums) -1 
            while l < r:
                left_val, right_val = nums[l], nums[r]
                threesum = nums[i] + left_val + right_val
            
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-= 1
                    # now have to move the pointer since we don't want duplicates if there is a case where the same values are in there
                    while l < r and nums[l] == left_val:
                        l += 1
        return res 
        # -2, 0, 1, 1, 2


