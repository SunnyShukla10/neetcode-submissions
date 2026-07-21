class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute force
        # count the array into a dict and check which value is > [n/2]

        # TIme O(N) and Space O(1)
        # Boyer - Moore Method

        res, count = nums[0], 0

        for i in range(len(nums)):
            # Different Element
            if i > 0 and nums[i-1] != nums[i]:
                count -= 1

                if count == 0:
                    res = nums[i]
          
            count += 1

        return res