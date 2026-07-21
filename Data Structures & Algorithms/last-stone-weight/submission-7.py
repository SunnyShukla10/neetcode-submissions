class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x  in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if abs(x-y) == 0:
                continue
            
            heapq.heappush(heap, -abs(x-y))

        return -heap[0] if heap else 0