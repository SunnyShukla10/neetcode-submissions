class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            # start of a sequence
            if num - 1 not in nums_set:
                print(f"{num} is a start of a squence")
                count = 1
                while num + count in nums_set:
                    count += 1

                max_len = max(max_len, count)
        return max_len