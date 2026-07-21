class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 1 2 3 4 5
        # 2 3 4 5 1
        # 3 4 5 1 2
        # 4 5 1 2 3
        # 5 1 2 3 4

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]: # left sorted portion
                # now have to figure out if we go right or left
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1 
