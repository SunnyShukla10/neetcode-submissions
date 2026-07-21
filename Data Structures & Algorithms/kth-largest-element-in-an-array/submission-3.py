class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
    
        while len(nums) != k - 1:
            val = heapq.heappop(nums)
        
        return val