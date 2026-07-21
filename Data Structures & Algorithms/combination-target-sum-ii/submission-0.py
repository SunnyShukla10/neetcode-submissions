class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        def backtrack(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return 

            if total > target or i >= len(candidates):
                return
            
            # decision 1: choose curr element
            combo.append(candidates[i])
            backtrack(i + 1, combo, total + candidates[i])
            combo.pop()

            # decision 2: choose another elem
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, combo, total)

        backtrack(0, [], 0)
        return res