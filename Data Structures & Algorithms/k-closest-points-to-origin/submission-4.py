class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pair in points:
            x,y = pair[0], pair[1]
            dist = math.sqrt((x)**2 + (y)**2)
            heap.append((dist, [x,y]))

        heapq.heapify(heap)

        res = []
        while heap:
            k-=1
            val = heapq.heappop(heap)
            res.append(val[1])
            
            if k == 0:
                return res
        
        