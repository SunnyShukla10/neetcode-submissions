class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        combo = []
        def backtrack(i, combo):
            val_sum = sum(combo)

            if val_sum == target:
                if combo not in res:
                    res.append(combo[:])
                return

            if val_sum > target or i == len(nums):
                return

            for i in range(len(nums)):
                combo.append(nums[i])

                # choice 1: choose current num
                backtrack(i, sorted(combo))

                # choice 2: choose next elem
                backtrack(i + 1, sorted(combo))
                combo.pop()

        backtrack(0, [])
        return res