class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums): # get idx and val
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums)- 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                    print("Three Sum > 0: ", r)
                elif three_sum < 0:
                    l += 1
                    print("Three Sum < 0: ", l)

                else: # equals 0!
                    res.append([a,nums[l], nums[r]])
                    print("Appended!")
                    l += 1
                    # make sure we skip past the same number
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                        print("Skipping past the same num, at index ", l)
            
        return res