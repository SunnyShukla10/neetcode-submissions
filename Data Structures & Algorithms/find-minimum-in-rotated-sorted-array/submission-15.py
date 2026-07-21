class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        min_val = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break
            
            m = (r + l) // 2
            min_val = min(nums[m], min_val)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        return min_val