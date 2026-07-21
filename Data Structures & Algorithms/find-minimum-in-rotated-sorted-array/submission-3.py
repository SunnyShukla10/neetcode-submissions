class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [ 1 2 3 4 5 ]
        # [ 3 4 5 1 2 ]
        # [ 5 1 2 3 4 ]

        res = nums[0]

        l , r = 0, len(nums) -1 

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = ((r-l) // 2 ) + l
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return res
