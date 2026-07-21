class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get mod k
        k = k % len(nums)
        
        # first reverse nums
        nums.reverse()
        
        # then reverse up until k
        l, r = 0, k-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1 
        
        r = len(nums)-1
        # then reverse after k
        while k < r:
            nums[k], nums[r] = nums[r], nums[k]
            r -= 1
            k += 1
