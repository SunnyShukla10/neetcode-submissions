class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # choice 1
            backtrack(i+1)

            # choice 2
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop() # undo
        
        backtrack(0)
        return res