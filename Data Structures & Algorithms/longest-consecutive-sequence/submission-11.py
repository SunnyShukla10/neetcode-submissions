class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        
        for i in nums:
            curRes = 0
            if i - 1 not in nums:
                while i in nums:
                    i += 1
                    curRes += 1
                res = max(curRes, res)

        return res
			