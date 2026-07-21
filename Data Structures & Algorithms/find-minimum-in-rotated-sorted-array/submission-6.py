class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''
        1 2 3 4 5 6
        6 1 2 3 4 5 
        5 6 1 2 3 4
        4 5 6 1 2 3 
        3 4 5 6 1 2  
        2 3 4 5 6 1 

        
                


        '''
        l, r = 0, len(nums) - 1
        res = nums[0]
        print(nums)
        while l <= r:
            m = (l + r) // 2
            print(f"value at idx {m} is {nums[m]}")
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
                res = min(res, nums[m])
        return res
