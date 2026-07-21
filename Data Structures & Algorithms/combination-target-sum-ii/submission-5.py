class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []

        def backtrack(i, total):
            print(total)
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            # choice 1 - use curr one
            subset.append(candidates[i])
            backtrack(i+1, total + candidates[i])
            subset.pop()

            # choice 2 go to the next one
            # want to make sure we go over the duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, total)

        backtrack(0,0)
        return res
        
        candidates=[1,2,3,4,5]