class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []


        def backtrack(i, total):
            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(subset.copy())
                return
            
            # choice 1 - use current one only
            subset.append(nums[i])
            backtrack(i, total + nums[i])
            subset.pop()

            # choice 2 - skip and choose another one 
            backtrack(i+1, total)
        
        backtrack(0,0)
        return res