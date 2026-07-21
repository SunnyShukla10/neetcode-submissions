class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # 2 2 3 4 6
        # 2 2 2 2 2
        # Need to keep inverting sign
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            
            # Since it's negative
            if x < y:
                heapq.heappush(max_heap, x-y)
        max_heap.append(0)
        return abs(max_heap[0])   