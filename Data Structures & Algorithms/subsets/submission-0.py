class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res = []
        subset = []

        def backtrack(idx):
            
            if idx == len(nums):
                res.append(subset[:])
                return  
            
            # Choice 1: Do not choose
            backtrack(idx + 1)

            # Choice 2: Choose 
            subset.append(nums[idx])
            backtrack(idx + 1)

            # undo choice
            subset.pop()
        
        backtrack(0)
        return res

