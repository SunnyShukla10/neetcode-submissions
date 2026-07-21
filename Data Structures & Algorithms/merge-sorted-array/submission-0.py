class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # First add the elemends to the end of nums1 arr
        # Run a counting sort --> can be bad since max(nums1) can be pretty huge


        # run 3 pointers:
        #   1. have a pointer that's at the end of nums2 array
        #   2. Have a pointer end of nums1 (before the first 0)
        #   3. Have a pointer end of nums1 

        # iterate through the array using the pointers
        # If the value of 1st pointer is > val of 2nd pointer --> add into the pointer 3 idx and decrement the pointer 3 
        # else: add end of 


        i = m-1
        j = n-1
        
        r = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[r] = nums1[i]
                i-=1
            else:
                nums1[r] = nums2[j]
                j-=1 
            r-= 1
        
        # fill leftover values
        while j >= 0:
            nums1[r] = nums2[j]
            j -= 1
            r -= 1



            
                


