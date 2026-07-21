class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_streak = 1
            
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_streak += 1
                
                res = max(cur_streak, res)

        return res