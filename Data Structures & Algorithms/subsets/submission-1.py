class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice one don't include curr val
            backtrack(i+1)

            # choice 2  include curr val
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
        backtrack(0)
        return res