class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision 1: Create all subsets that include this num
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # Decision 2: Create all subsets that don't include this val
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
            
        
        backtrack(0)
        return res