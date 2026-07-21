class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1
        idx = 0
        # iterate until i > len(count) has nothing
        for i in range(3):    
            while count[i] > 0:
                count[i] -= 1
                nums[idx] = i
                idx += 1

