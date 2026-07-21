class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] 
        for i, num in enumerate(nums):
            ans.insert(i, num)
            ans.insert(i + len(nums), num)

        return ans