class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        if n == 1:
            return nums
        
        # Divide
        m = n // 2
        L = self.sortArray(nums[:m])
        R = self.sortArray(nums[m:])

        # Merge
        sorted_arr = [0] * n
        l, r, i = 0, 0, 0

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
            
            i += 1

        # left over
        while l < len(L):
            sorted_arr[i] = L[l]
            l += 1
            i += 1

        while r < len(R):
            sorted_arr[i] = R[r]
            r += 1
            i += 1
        print(sorted_arr)
        return sorted_arr