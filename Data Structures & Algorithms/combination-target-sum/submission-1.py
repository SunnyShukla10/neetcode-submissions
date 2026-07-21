class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
       
        def backtrack(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if total > target or i == len(nums):
                return

            # Decision 1: Use the current value
            combo.append(nums[i])
            backtrack(i, combo, total + nums[i])
            combo.pop()
            
            # Decision 2: Use the next value
            backtrack(i + 1, combo, total)

            # for i in range(len(nums)):
            #     combo.append(nums[i])

            #     # choice 1: choose current num
            #     backtrack(i, combo, total + nums[i])

            #     # choice 2: choose next elem
            #     backtrack(i + 1, combo, total + nums[i])
            #     combo.pop()

        backtrack(0, [], 0)
        return res