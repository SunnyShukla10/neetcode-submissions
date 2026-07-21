class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)

            diff = abs(val1-val2)

            if diff != 0:
                heapq.heappush(max_heap, -diff)
        
        return -max_heap[0] if max_heap else 0 