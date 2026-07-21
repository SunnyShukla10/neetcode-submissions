class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [-x for x in nums]

        heapq.heapify(min_heap)

        for i in range(k):
            res = heapq.heappop(min_heap)
        
        return -res