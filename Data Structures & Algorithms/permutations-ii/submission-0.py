class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)

        res, subset = [], []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
            
            for c in count:
                if count[c] > 0:
                    subset.append(c)
                    count[c] -= 1

                    dfs()

                    subset.pop()
                    count[c] += 1
            
        dfs()
        return res 
