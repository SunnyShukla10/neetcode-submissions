class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # no dups, O(1) lookup time
        nums_set: set = set(nums)
        longest: int = 0
        # need to find out the start of the subsequence, if there exists a val - 1 in the set, then that's the start
        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                
                longest = max(longest, length)

        return longest
                
            
