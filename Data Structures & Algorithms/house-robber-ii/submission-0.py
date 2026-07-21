class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])


        def house_rob1(l, r):
            one, two = 0, 0

            while l <= r:
                num = nums[l]

                temp = max(one + num, two)
                one = two
                two = temp
                l+= 1
            
            return two
        

        max1 = house_rob1(0, len(nums)-2)
        max2 = house_rob1(1, len(nums)-1)

        return max(max1, max2)